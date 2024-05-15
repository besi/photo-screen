#!/usr/bin/env python3

from icloudphotos import icloudphotos
from settings import settings
from appstate import appstate

def main():
    general_settings = settings.load_settings('general.settings')
    photos_dir = general_settings.get('photos_dir')
    icloudphotos_settings = settings.load_settings('icloudphotos.settings')
    new_photos = icloudphotos.download_album(icloudphotos_settings['album_url'], photos_dir)

    print(f"New Photos (icloud album): {new_photos}")

    if new_photos:
        photo_name = appstate.appstate_new()
        print(photo_name)


if __name__ == "__main__":
    main()