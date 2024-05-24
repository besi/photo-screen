import os
import json
import fcntl

def lock_file(file):
    """ Lock the file for writing in a Unix-based system. """
    fcntl.flock(file.fileno(), fcntl.LOCK_EX)

def unlock_file(file):
    """ Unlock the file. """
    fcntl.flock(file.fileno(), fcntl.LOCK_UN)

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
            lock_file(file)
            json.dump(settings, file, indent=4)
            unlock_file(file)
    except:
        print(f'error writing file: {settings_path}')
        unlock_file(file)

def delete_settings(filename):
    # Construct the path to the settings file
    home_dir = get_settings_path()
    settings_path = os.path.join(home_dir, filename)
    os.system(f'rm {settings_path}')