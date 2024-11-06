import requests
import json

class PxWeb:
    def __init__(self, url):
        self.url = url
        
    def fetch(self):
        try:
            return requests.get(self.url)
        except Exception as e:
            print(f'Error: {e}')
                
    def post(self, body):
        try:
            return requests.post(self.url, json=body)                
        except Exception as e:
            print(f'Error: {e}')