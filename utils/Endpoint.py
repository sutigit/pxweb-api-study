class Endpoint:
    def __init__(self, url):
        self.url = url.rstrip('/')
    
    def get_current(self):
        return self.url