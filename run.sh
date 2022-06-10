#!/bin/sh
echo "* * * * * find /opt/screen-recorder/media/* -type d -cmin +$MEDIA_DURATION -exec rm -rf {} +" | crontab -
service cron start
python run.py
