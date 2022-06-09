#!/bin/sh
echo "0 * * * * find /opt/screen-recorder/media/* -name '*.mp4' -exec rm {} +" | crontab -
#echo "0 * * * * find /opt/screen-recorder/media/* -name '*.mp4' -ctime +MEDIA_DURATION -exec rm {} +" | crontab -
service cron start
python run.py
