#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from time import gmtime, strftime
from ConfigParser import SafeConfigParser


class log(object):
    def __init__(self):
        # Read Configfile
        config = SafeConfigParser()
        config.read('server-sleep.cfg')
        self.mode = int(config.get('log', 'mode'))
        self.path = config.get('log', 'file')
        self.printanyway = int(config.get('log', 'printanyway'))

        if (self.path != ""):
            self.logfile = open(self.path, 'a')

    def __del__(self):
        self.logfile.close()

    def log(self, message, type_=3, important=False):
        if (type_ <= self.mode) or (self.mode != 0 and important == True):
            type_str = None;
            if type_ == 1:
                type_str = " ERROR:   "
            elif type_ == 2:
                type_str = " WARNING: "
            elif type_ == 3:
                type_str = " INFO:    "
            elif type_ == 4:
                type_str = " DEBUG:   "
            else:
                type_str = " UNKNOWN: "

            if (self.path == "" or self.printanyway == 1):
                print(strftime("%Y-%m-%d %H:%M:%S", gmtime()) + type_str + message)
            if (self.path != ""):
                try:
                    self.logfile.write(strftime("%Y-%m-%d %H:%M:%S", gmtime()) + type_str + message)
                except:
                    print(" ERROR:  Can't access logfile!")
