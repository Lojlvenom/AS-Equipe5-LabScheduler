#!/bin/bash
sudo chmod a+x . 
cd "$(dirname "$0")"
python email_notification.py