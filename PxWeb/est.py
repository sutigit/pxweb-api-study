from .parent import Parent

class PWE(Parent):
    def __init__(self, lang, *args):
        
        url = f'https://andmed.stat.ee/api/v1/{lang}/stat/'
        url_out = f'https://andmed.stat.ee/{lang}/stat'
        
        super().__init__(url, url_out, lang, *args)