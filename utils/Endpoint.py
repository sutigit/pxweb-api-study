import re

"""
This class breaks the given URL into its components and stores them in self.__url_object for easy access.
The components are broken down adhering to the strcutre provided in the PxWeb API documentation.
The components are:
- name: The name of the API
- version: The version of the API
- language: The language of the API
- database_id: The database ID of the API
- levels: The levels of the API
- table_id: The table ID of the API

See https://pxdata.stat.fi/API-description_SCB.pdf for more information.
"""
class Endpoint:
    def __init__(self, url):
        chunks = re.split(r'(v\d+/)', url, maxsplit=1)
        api_name = chunks[0].rstrip('/') if chunks[0] else None
        api_version = chunks[1].rstrip('/') if chunks[1] else None
        rest = chunks[2].split('/') if chunks[2] else []
        api_language = rest[0] if rest[0] else None
        api_database_id = rest[1] if rest[1] else None
        
        api_levels = {}
        api_table_id = None
        
        for index, chunk in enumerate(rest[2:]):
            if chunk.endswith('.px'):
                api_table_id = chunk
            else:
                api_levels[f"level_{index+1}"] = chunk
        
        self.__url_object = {
            'url': url,
            'name': api_name,
            'version': api_version,
            'language': api_language,
            'database_id': api_database_id,
            'levels': api_levels,
            'table_id': api_table_id
        }
        
            
    def get_url(self):
        return self.__url_object['url']
    
    def get_name(self):
        return self.__url_object['name']
    
    def get_version(self):
        return self.__url_object['version']
    
    
    # Language setting and getting
    def get_language(self):
        return self.__url_object['language']
    
    def set_language(self, language):
        self.__url_object['language'] = language
    
    
    # Database ID setting and getting
    def get_database_id(self):
        return self.__url_object['database_id']
    
    def set_database_id(self, database_id):
        self.__url_object['database_id'] = database_id
    
    
    # Levels setting and getting
    def get_levels(self):
        return self.__url_object['levels']
    
    def set_level(self, level, level_id):
        self.__url_object['levels'][f'level_{level}'] = level_id
        
    
    # Table ID setting and getting
    def get_table_id(self):
        return self.__url_object['table_id']
    
    def set_table_id(self, table_id):
        self.__url_object['table_id'] = table_id
