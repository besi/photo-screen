""" 
Mock inky display for running on desktop
"""
class InkyMock:

    resolution = (600, 488)
    BLACK = 0
    WHITE = 1

    def __init__(self, image = None):
        self.image = image

    def set_image(self, new_image, saturation=0.5):
        self.image = new_image
    
    def set_border(self, param):
        # do nothing
        return None
    
    def show(self):
        if self.image:
            self.image.show()