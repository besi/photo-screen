#!/usr/bin/env bash

if IMAGE=`ls -1 /home/pi/photo-screen/photos/*.jpg  | shuf -n 1`
if [ $? -eq 0 ]; then
    echo OK
else
    echo FAIL
fi
  echo -e "Has length, and contain only whitespace  \"$str\"" 
  mv /home/pi/photo-screen/photos_old/* /home/pi/photo-screen/photos/
else
    echo "all good"
fi
# else
#    echo $IMAGE
#    /home/pi/inky/examples/7color/image.py $IMAGE
#    mv $IMAGE /home/pi/photo-screen/photos_old
#fi
