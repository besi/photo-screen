Download images
---------------

    ./download-album http://icloud.com/shared-album/xyz/ photos


Cronjob
-------


    # Change the photo every day at 3am
    0 3 * * * /home/pi/photo-screen/bin/change_photo.py

    # Testing: Change it every 25 Minutes
    */25 * * * * /home/pi/photo-screen/bin/change_photo.py
