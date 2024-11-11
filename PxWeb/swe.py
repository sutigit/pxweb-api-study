from .base import Base

class PWS(Base):
    def __init__(self, lang, *args):
        
        url = f'https://api.scb.se/OV0104/v1/doris/{lang}/ssd/'
        url_out = f'http://www.statistikdatabasen.scb.se/pxweb/{lang}/ssd/START__'
        
        super().__init__(url, url_out, *args)