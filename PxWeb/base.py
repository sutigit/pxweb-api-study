from . import session
import json

from .num_utils import log_scale
from .num_utils import inverse_log_scale
from .num_utils import get_split_points
from .num_utils import progressive_rounding

"""
See Docs of this Class pattern from: https://github.com/kirajcg/pyscbwrapper/blob/master/pyscbwrapper_en.ipynb
"""

class Base(object):
    def __init__(self, url, url_out, *args):
        self.ids = list(args)
        self.url = url
        self.url_out = url_out
        self.query = {
            "query": [], 
            "response": {"format": "json"}
        }

    def info(self):
        """ Returns the metadata associated with the current folder. """
        response = session.get(self.url + '/'.join(self.ids))
        return response.json()

    def go_down(self, *args):
        """ Goes deeper in the hierarchical metadata structure. """
        self.ids += list(args)

    def go_up(self, k=1):
        """ Goes k levels up in the hierarchical metadata structure. """
        self.ids = self.ids[:-k]

    def get_url(self):
        """ Returns the url to the current folder. """
        if len(self.ids[-1]) >= 3:
            try:
                int(self.ids[-1][3])
            except ValueError:
                return self.url_out + '__'.join(self.ids[:-1]) + '/' + self.ids[-1]
        return self.url_out + '__'.join(self.ids)

    def get_variables(self):
        """ Returns a dictionary of variables and their ranges for the bottom node. """
        response = self.info()
        val_dict = {}
        try:
            variables = response['variables']
        except TypeError:
            print("Error: You are not in a leaf node.")
            return
        for item in variables:
            val = list(item.values())
            for i in range(1, len(val), 4):
                for j in range(3, len(val), 4):
                    val_dict[val[i]] = val[j]
        return val_dict

    def clear_query(self):
        """ Clears the query. Mostly an internal function to use in others. """
        self.query = {
            "query": [], 
            "response": {"format": "json"}
        }

    def set_query(self, **kwargs):
        """ Forms a query from input arguments. """
        self.clear_query()
        response = self.info()
        variables = response['variables']
        for kwarg in kwargs:
            for var in variables:
                if var["text"].replace(' ' , '') == kwarg:
                                        
                    if type(kwargs[kwarg]) == list:
                        values = [
                            var['values'][j] \
                            for j in range(len(var['values'])) \
                            if var['valueTexts'][j] in kwargs[kwarg]
                        ]
                        
                    elif type(kwargs[kwarg]) == str:
                        values = [
                            var['values'][j] \
                            for j in range(len(var['values'])) \
                            if var['valueTexts'][j] == kwargs[kwarg]
                        ]
                        
                    self.query["query"].append({
                            "code": var['code'],
                            "selection": {
                                    "filter": "item",
                                    "values": values
                                    }
                                })

    def get_query(self):
        """ Returns the current query. """
        return self.query

    def get_data(self):
        """ Returns the data from the constructed query. """
        response = session.post(self.url + '/'.join(self.ids), json = self.query)
        response_json = json.loads(response.content.decode('utf-8-sig'))
        return response_json
    
    
    def data_to_timeseries(self, data):
        """ 
        Converts the data to a timeseries object.
        
        The timeseries data is structured as follows:
        tsdata= {
            meta: {
                minYear: number,
                maxYear: number,
                minValue: number,
                maxValue: number,
                choropleth_tresholds: [number, number, ...],
            }
            regiondata: {
                'code1': {
                    'year1': number,
                    'year2': number,
                    ...
                },
                'code2': {
                    'year1': number,
                    'year2': number,
                    ...
                },
                ...
            }
        } 
        
        @param data: The data from the get_data() function.
        @type data: dict
        @return: The timeseries data.
        
        """        
        tsdata = {}
        
        codes = self.get_query()['query'][0]['selection']['values']

        # Building regiondic
        regiondic = {}
        for i in range(len(codes)):
            regiondic[codes[i]] = codes[i]
            
        
        # Meta informations        
        minYear = float('inf')
        maxYear = float('-inf')
        minValue = float('inf')
        maxValue = float('-inf')
        datavalues = []


        # Building regiondata and meta information
        regiondata = {}
        for code in regiondic:
            regiondata[regiondic[code]] = {}
            for i in range(len(data)):
                if data[i]['key'][0] == code:
                    year = data[i]['key'][1]
                    value = float(data[i]['values'][0]) if data[i]['values'][0] not in ['.', '..'] else None                    
                    
                    # regiondata
                    regiondata[regiondic[code]][year] = value
                    
                    # meta information
                    minYear = min(minYear, int(year))
                    maxYear = max(maxYear, int(year))
                    if value is not None:
                        minValue = min(minValue, value)
                        maxValue = max(maxValue, value)
                        
                        # datavalues for log scale split tresholds
                        datavalues.append(value)


        # Log scale the min and max values to compress the outliers in the datavalues
        log_scaled = log_scale([minValue, maxValue])
        
        # Calculate the split points for the log scaled values
        splits = get_split_points(min = log_scaled[0], max = [log_scaled[1]], splits = 5)
        
        # Inverse the log scale to get the original values
        original_scale = inverse_log_scale(splits)
        
        # Round the values to prettier numbers
        choropleth_tresholds = progressive_rounding(original_scale)
        
                    
        tsdata['meta'] = {
            'minYear': minYear,
            'maxYear': maxYear,
            'minValue': minValue,
            'maxValue': maxValue,
            'choropleth_tresholds': choropleth_tresholds
        }
        
        tsdata['regiondata'] = regiondata

        return tsdata