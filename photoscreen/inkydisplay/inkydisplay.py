#!/usr/bin/python3

""" 
Displays an image on the inky screen
arg 1: image-file

can resize, rotate, pad or crop the image to fit the screen
"""

from PIL import Image, ImageOps
from .inkymock import InkyMock
import os

def dynamic_import(module_name, function_name):
    try:
        module = __import__(module_name, fromlist=[function_name])
        func = getattr(module, function_name)
        return func
    except (ImportError, AttributeError) as e:
        print(f"Error importing {function_name} from {module_name}: {e}")
        return None

def is_module_available(module_name):
    try:
        __import__(module_name)
        return True
    except ImportError:
        return False

def show_image(photo_name, photos_dir, settings, mode=None):
    filepath = os.path.join(photos_dir, photo_name)
    return show_imagepath(filepath, settings, mode)
    

def show_imagepath(filepath, settings, mode=None):
    saturation = settings.get('saturation', 0.5)
    orientation = settings.get('orientation', 'landscape')

    if mode == None:
        mode = settings.get('mode', 'zoom')

    inky_auto = dynamic_import('inky.auto', 'auto')
    if inky_auto:
        display = inky_auto(ask_user=True, verbose=True)
    else:
        display = InkyMock()
    image = Image.open(filepath)
    image = ImageOps.exif_transpose(image)
    
    if orientation == 'portrait':
        image = image.transpose(Image.Transpose.ROTATE_90)
    
    if mode == 'auto':
        if image.height > image.width:
            mode = 'letterbox'
        else:
            mode = 'zoom'
    
    if mode == 'letterbox':
        resized_image = ImageOps.pad(image, display.resolution, color="#fff")
    else:
        resized_image = ImageOps.fit(image, display.resolution)
    
    display.set_image(resized_image, saturation=saturation)
    display.set_border(display.WHITE)
    display.show()
    return mode

if __name__ == "__main__":
    import sys

    photo_path = sys.argv[1]
    show_imagepath(photo_path)
