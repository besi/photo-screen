#!/usr/bin/env python3

""" 
Script to fetch images from imap, icloud photos, etc.
expects settings files to be present under ~/.photoscreen/
"""

from icloudphotos import icloudphotos
from imap import imap
from settings import settings
from appstate import appstate

def check_icloud(photos_dir):
    icloudphotos_settings = settings.load_settings('icloudphotos.settings')
    new_photos = icloudphotos.download_album(icloudphotos_settings['album_url'], photos_dir)

    print(f"New Photos (icloud album): {new_photos}")
    return new_photos

def check_imap(photos_dir):
    imap_settings = settings.load_settings('imap.settings')
    new_photos = imap.fetch_email(imap_settings, photos_dir)

    print(f"New Photos (imap): {new_photos}")
    return new_photos

def main():
    new_photos = []
    general_settings = settings.load_settings('general.settings')
    photos_dir = general_settings.get('photos_dir')
    
    if general_settings.get('icloudphotos') == 'on':
        new_photos.extend(check_icloud(photos_dir))
    
    if general_settings.get('imap') == 'on':
        new_photos.extend(check_imap(photos_dir))

    if new_photos:
        photo_name = appstate.appstate_new()
        print(photo_name)

if __name__ == "__main__":
    main()