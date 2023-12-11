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

