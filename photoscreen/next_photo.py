#!/usr/bin/env python3

""" 
Script for displaying the next photo
expects settings files to be present under ~/.photoscreen/
"""

from appstate import appstate

def main():
    photo_name = appstate.appstate_next()

    # reshuffle photos when end is reached
    if not photo_name:
        photo_name = appstate.appstate_new()

if __name__ == "__main__":
    main()