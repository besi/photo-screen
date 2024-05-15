import os
import json

def get_settings_path():
    return os.path.expanduser('~/.photoscreen')

def load_settings(filename):
    # Construct the path to the settings file
    home_dir = get_settings_path()
    settings_path = os.path.join(home_dir, filename)
    
    # Read and parse the settings file
    try:
        with open(settings_path, 'r') as file:
            settings = json.load(file)
            return settings
    except FileNotFoundError:
        print(f"File {settings_path} not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error decoding JSON from the file {settings_path}")
        return None
    except Exception:
        print(f"Error: {Exception}")
        return None

def save_settings(filename, settings):
    home_dir = get_settings_path()
    settings_path = os.path.join(home_dir, filename)
    try:
        with open(settings_path, 'w') as file:
            json.dump(settings, file, indent=4)
    except:
        print(f'error writing file: {settings_path}')