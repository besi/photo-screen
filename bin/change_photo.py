#!/usr/bin/python3

import os
import random
import glob

dir = '/home/pi/photo-screen/photos'
dir_old = f"{dir}_old"

def get_photos(photos, dir):
    types = ('*.jpg', '*.png')
    for files in types:
        photos.extend(glob.glob(f"{dir}/{files}"))
    return photos

photos = []
photos = get_photos(photos, dir)
if len(photos) == 0:
    print("Start afresh...")
    os.system(f"mv {dir_old}/* {dir}/")
    photos = get_photos(photos, dir)

# Pick a random file
photo = random.choice (photos)
print(photo)

os.system(f"/home/pi/inky/examples/7color/image.py {photo}")
os.system(f"mv {photo} {dir_old}")
