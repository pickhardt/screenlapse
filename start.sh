#!/usr/bin/env sh

./stop.sh

echo "Starting screenlapse as daemon"
python screenlapse.py&