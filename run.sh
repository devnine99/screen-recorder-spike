#!/bin/sh
echo "0 * * * * find /opt/screen-recorder/media/* -type d -cmin +1 rm {} +" | crontab -
#echo "0 * * * * find /opt/screen-recorder/media/* -name '*.mp4' -ctime +MEDIA_DURATION -exec rm {} +" | crontab -
service cron start
python run.py
