from inkydisplay import inkydisplay
from settings import settings

def show_imagepath(image_path):
    general_settings = settings.load_settings('general.settings')
    inkydisplay.show_imagepath(image_path, general_settings)

if __name__ == "__main__":
    import sys

    photo_path = sys.argv[1]
    show_imagepath(photo_path)

