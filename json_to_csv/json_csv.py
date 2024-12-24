import json 
import csv



class JsonToCsv:
    
    def __init__(self, json_file: str= None, csv_file: str =None):
        self.json_file  = json_file
        self.csv_file   = csv_file
        self.json_data = None
        self.flattend_data = []
        self.headers = []
        
    def load_json(self):
        
        try:
            with open(self.json_file, 'r') as f:
                self.json_data = json.load(f)
            print("Json loaded successfully")

        except Exception as e:
            print(e)


    def flatten(self, data, parent_key='', sep='_'):
        items = []
        for k, v in data.items():
            new_key = parent_key + sep + k if parent_key else k