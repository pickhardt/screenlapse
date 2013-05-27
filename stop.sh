#!/usr/bin/env sh

pid_file=timelapse.pid

if [ -f ${pid_file} ]
then
  echo "Stopping timelapse"
  sudo kill `cat ${pid_file}`
  rm ${pid_file}
fi