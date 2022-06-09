#!/bin/sh
echo "* * * * * find /opt/screen-recorder/media/* -type d -cmin +60 -exec rm -rf {} +" | crontab -
service cron start
python run.py
