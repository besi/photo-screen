mkdir /home/pi/photo-screen/photos
mkdir /home/pi/photo-screen/photos_old
# Software update
sudo cp etc/software-update.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable software-update
sudo systemctl start software-update
