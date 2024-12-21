from shutil import move
import os 
from pathlib import Path
import sys
import json
import logging

logging.basicConfig(level=logging.INFO)

def log_action(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Executing {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"Completed {func.__name__}")
        return result
    return wrapper



class Arange:
    
    # load folder-extension mappings from config.json file
    @staticmethod
    @log_action
    def load_config(filename : str = "config.json") -> dict:
        '''
        Load folder-extension mappings from json file
        :param filename: Name of the JSON configuration file (default: 'config.json')
        :return: A dictionary containing folder-extension mappings
        '''
        try:
            with open(filename, 'r') as file:       #contextmanager used
                directory = json.load(file)
                
                if not isinstance(directory, dict):         # validation to check if json is correctly formatted
                    print(f"Error:Invalid JSON format in '{filename}'. Please check your configuration file.")
                    sys.exit(1)
                return directory
        except FileNotFoundError:
            print(f"Error: {filename} not found.")
            sys.exit(1)
        return {}
    
    #create folders based on extension mapping
    @staticmethod
    @log_action
    def create_folders(directory:str) -> str:
        for dir in directory.keys():
            try:
                os.makedirs(dir,exist_ok=True) 
                print(f"{dir} created or already exists")
            except OSError as e:
                print(f"Error creating folder '{dir}': {e}")

    
    
    #Deteremine which folder a file belongs to
    @staticmethod
    @log_action
    def get_folder(ext:str,directory: dict) ->str:
        ext.lower()
        for folder, extension in directory.items():
            if ext in extension:
                return folder
        return 'other'
    
    #start moving files based on their extension
    @staticmethod
    @log_action
    def start(directory: dict, target_dir: str = ".", dry_run: bool = False):
        for filename in os.listdir(target_dir):
            file_path = os.path.join(target_dir, filename)
            if os.path.isdir(file_path):
                continue
            ext = os.path.splitext(filename)[1].lower()
            print(f"Processing file: {filename}, Extracted extension: {ext}")
            folder = Arange.get_folder(ext, directory)
            print(f"File {filename} will be moved to folder: {folder}")
            target_path = os.path.join(target_dir, folder)
            if not os.path.exists(target_path):
                os.makedirs(target_path, exist_ok=True)
            if dry_run:
                print(f"Would move {file_path} to {os.path.join(target_path, filename)}")
            else:
                move(file_path, os.path.join(target_path, filename))

if __name__ == "__main__":
    directory = Arange.load_config()
    Arange.create_folders(directory)
    Arange.start(directory, dry_run=True)


