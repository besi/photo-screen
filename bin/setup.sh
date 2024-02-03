mkdir /home/pi/photo-screen/photos
mkdir /home/pi/photo-screen/photos_old

# Image downloader
python3 -m pip install click pyicloud pytz


# Inky
sudo apt-get install python3-pip git imagemagick libopenjp2-7-dev jq -y 
sudo rm -rf /usr/lib/python3.11/EXTERNALLY-MANAGED
pip3 install inky[rpi,example-depends]
curl https://get.pimoroni.com/inky | bash

cd
git clone https://github.com/pimoroni/inky


# Software update
sudo cp software-update.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable software-update
sudo systemctl start software-update
sudo service cron start
