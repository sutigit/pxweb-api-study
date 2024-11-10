from .parent import Parent

class PWN(Parent):
    def __init__(self, lang, *args):
        
        url = f'https://data.ssb.no/api/v0/{lang}/table/'
        url_out = f'https://www.ssb.no/{lang}/statbank/'
        
        super().__init__(url, url_out, lang, *args)