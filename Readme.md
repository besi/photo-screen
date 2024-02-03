Installation
------------

    python3 -m pip install click pyicloud pytz

Install the startup service

    sudo mv photo-screen.service /etc/systemd/system/
    sudo systemctl daemon-reload
    sudo systemctl enable photo-screen
    sudo systemctl start photo-screen

Download images
---------------

    ./download-album http://icloud.com/shared-album/xyz/ photos


Cronjob
-------


    # Change the photo every day at 3am
    0 3 * * * /home/pi/photo-screen/bin/change_photo.py

    # Testing: Change it every 25 Minutes
    */25 * * * * /home/pi/photo-screen/bin/change_photo.py
