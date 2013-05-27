#!/usr/bin/env sh

./stop.sh

echo "Starting timelapse as daemon"
python timelapse.py&