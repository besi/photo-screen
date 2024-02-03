#!/usr/bin/env bash

# cd -- "$(dirname "$0")" >/dev/null


IMAGE=`ls -1 /home/pi/photo-screen/photos/*.jpg  | shuf -n 1`
echo $IMAGE
/home/pi/inky/examples/7color/image.py $IMAGE
echo "TODO: delete image now $IMAGE"
