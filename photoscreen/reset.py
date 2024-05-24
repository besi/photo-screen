#!/usr/bin/env python3

from appstate import appstate

if __name__ == "__main__":
    print("Deleting all photos and app state...")
    appstate.reset_and_delete()

