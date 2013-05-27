#!/usr/bin/env sh

pid_file=screenlapse.pid

if [ -f ${pid_file} ]
then
  echo "Stopping screenlapse"
  sudo kill `cat ${pid_file}`
  rm ${pid_file}
fi