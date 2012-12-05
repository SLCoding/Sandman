#!/usr/bin/env python
#-*- coding: utf-8 -*-
import sys, os, time
import importlib

from ConfigParser import SafeConfigParser
from log import log
sys.path.append("check-modules/")

class serverSleep (object):
	def __init__(self):
		# Read Configfile
		config = SafeConfigParser()
		config.read('server-sleep.cfg')
		self.checkinterval = int(config.get('serverSleep', 'checkinterval'))
		self.sleepcmd = config.get('serverSleep', 'sleepcmd')
		self.enabledmodules = eval(config.get('serverSleep', 'enabledmodules'))
		self.modules = []
		self.logger = log()
		
		for enabledmodule in self.enabledmodules:
			module = importlib.import_module(enabledmodule, enabledmodule)
			self.modules.append(module)
			
	def __del__(self):
		pass
	
	def startup (self):
		while True:	
			self.logger.log ("Wait " + str(self.checkinterval) + " seconds...")
			time.sleep(self.checkinterval)
			
			result = True
			
			self.logger.log ("Checks started")
			status = None
			for module in self.modules:
				name = self.enabledmodules[self.modules.index(module)]
				status = getattr(module, name).run()

				if status == 1:
					result = False
				elif status == 2:
					result = True
					break
				elif status ==  -1:
					self.logger.log (name + " failed!", 1)
			
			if (result == False):
				continue

			self.logger.log("All Checks OK: Going to Sleep Now!", 3, True)
			os.system(self.sleepcmd);
			self.logger.log("Sleep is over: Server woke up!", 3, True)