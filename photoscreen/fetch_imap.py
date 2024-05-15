#!/usr/bin/env python3

from imap import imap
from settings import settings
from appstate import appstate

def main():
    general_settings = settings.load_settings('general.settings')
    photos_dir = general_settings.get('photos_dir')
    imap_settings = settings.load_settings('imap.settings')
    new_photos = imap.fetch_email(imap_settings, photos_dir)

    print(f"New Photos (imap): {new_photos}")

    if new_photos:
        photo_name = appstate.appstate_new()
        print(photo_name)

if __name__ == "__main__":
    main()