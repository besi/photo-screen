#!/bin/bash

# Installs the default services (see services/) for running and scheduling 
# the photo screen tasks

echo "Copying services to /etc/systemd/system/"
sudo cp services/* /etc/systemd/system/

echo "Enabling services and timers with systemctl"

# Reload the systemd daemon to recognise the new service and timer files:
sudo systemctl daemon-reload

sudo systemctl enable handle_buttons.service

sudo systemctl enable next_photo.timer
sudo systemctl start next_photo.timer

sudo systemctl enable fetch_all.timer
sudo systemctl start fetch_all.timer

sudo systemctl enable wifi-power-save-off.timer
sudo systemctl start wifi-power-save-off.timer