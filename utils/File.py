import os
    
class File:
    def __init__(self, name, type='json'):
        self.name = name
        self.type = type
        
    def write(self, data):
        with open(f'{self.name}.{self.type}', 'w') as file:
            file.write(data)
            
    def read(self):
        with open(f'{self.name}.{self.type}', 'r') as file:
            return file.read()
            
    def delete(self):
        if os.path.exists(f'{self.name}.{self.type}'):
            os.remove(f'{self.name}.{self.type}')
        else:
            print("The file does not exist")