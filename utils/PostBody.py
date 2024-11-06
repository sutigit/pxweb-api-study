import json
            
class PostBody:
    def __init__(self, base):
        self.data = json.loads(base)
        
    def set_value_key(self, key_value: list):
        idx = 1
        self.data['query'][idx]['selection']['values'] = key_value
        
    def get(self):
        return self.data
    
    def get_json(self):
        return json.dumps(self.data)