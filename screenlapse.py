#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Takes timelapse screenshots and saves them to an output folder.
# Wequires the "screencapture" command, which should come with Macs.
# Made by Jeff Pickhardt (pickhardt@gmail.com)

import os
import datetime
import time

_DELAY = 20 # seconds
_PATH = "output/"
_PID_FILE = "screenlapse.pid"

def save_pid(pid_file_name):
  """Outputs the current pid to a pid file."""
  with open(pid_file_name, "w") as pid_file:
    pid_file.write(str(os.getpid()))

save_pid(_PID_FILE)

index = 0
while True:
  index += 1
  os.system("screencapture -C -x %spic%s.png" % (_PATH, index))
  time.sleep(_DELAY)
