""" 
Module for managing the state of the photoscreen
creates the files photos.index and app.state in order to persist the state
(in ~/.photoscreen), 2024 Marco Klingmann
"""

import os
from settings import settings
import random
from inkydisplay import inkydisplay

def read_appstate():
    index = settings.load_settings('photos.index')
    state = settings.load_settings('app.state')
    if index is None:
        index = []
    if state is None:
        state = {}
    return index, state

def save_appstate(index, state):
    settings.save_settings('photos.index', index)
    settings.save_settings('app.state', state)

def update_photos_index(index, photos_dir):
    all_files = os.listdir(photos_dir)
    
    # Create a set of existing file names
    existing_files = {photo['file'] for photo in index}
    
    # Add new photos, avoiding duplicates
    for file in all_files:
        if file not in existing_files:
            index.append({"file": file, "view_count": 0})
    
    # remove non-existing photos from index
    for photo in index:
        if photo['file'] not in all_files:
            index.remove(photo)
    
    return index


def sort_index(index):
    unseen = [photo for photo in index if photo['view_count'] == 0]
    already_seen = [photo for photo in index if photo['view_count'] > 0]
    
    # Sort Unseen by filename in descending order
    unseen = sorted(unseen, key=lambda photo: photo['file'], reverse=True)
    # shuffle arlready seen photos
    random.shuffle(already_seen)
    index = unseen + already_seen
    return index

def display_photo(photofile, mode=None):
    general_settings = settings.load_settings('general.settings')
    photos_dir = general_settings.get('photos_dir')

    mode = inkydisplay.show_image(photofile, photos_dir, general_settings, mode)
    return mode

def update_state(new_pos, index, state, mode=None):
    photo_to_display = index[new_pos]
    photo_to_display['view_count'] = photo_to_display['view_count'] + 1
    photofile = photo_to_display['file']
    
    new_mode = display_photo(photofile, mode=mode)

    #update state
    index[new_pos] = photo_to_display
    state = {'pos': new_pos, 'file': photofile, 'mode': new_mode}

    save_appstate(index, state)
    return photofile 


# new photos
def appstate_new():
    general_settings = settings.load_settings('general.settings')
    photos_dir = general_settings.get('photos_dir')

    index, state = read_appstate()

    index = update_photos_index(index, photos_dir)
    index = sort_index(index)

    if index:
        new_pos = 0
        return update_state(new_pos, index, state)
    
def appstate_next():
    index, state = read_appstate()

    pos = state.get('pos', 0)
    new_pos = pos + 1

    if 0 <= new_pos < len(index):
        return update_state(new_pos, index, state)

def appstate_prev():
    index, state = read_appstate()

    pos = state.get('pos', 0)
    new_pos = pos - 1
    if 0 <= new_pos < len(index):
        return update_state(new_pos, index, state)
    
def appstate_toggle_mode():
    index, state = read_appstate()

    new_pos = state.get('pos', 0)
    mode = state.get('mode', 'auto')
    if (mode == 'zoom'):
        override_mode = 'letterbox'
    if (mode == 'letterbox'):
        override_mode = 'zoom'
    
    if 0 <= new_pos < len(index):
        return update_state(new_pos, index, state, override_mode)

def reset_and_delete():
    general_settings = settings.load_settings('general.settings')
    photos_dir = general_settings.get('photos_dir')
    os.system(f'rm {photos_dir}/*')
    settings.delete_settings('photos.index')
    settings.delete_settings('app.state')
