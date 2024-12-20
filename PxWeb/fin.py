from .base import Base

class PWF(Base):
    def __init__(self, lang, *args):
        url = f'https://pxdata.stat.fi:443/PxWeb/api/v1/{lang}/'
        url_out = f'https://pxdata.stat.fi/PXWeb/pxweb/{lang}/StatFin/'
        
        super().__init__(url, url_out, *args)