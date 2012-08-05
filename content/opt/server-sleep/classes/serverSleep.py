#!/usr/bin/env python
#-*- coding: utf-8 -*-
from ConfigParser import SafeConfigParser
from log import log
sys.path.append("../check-modules/")

class serverSleep (object):
	def __init__(self):
		# Read Configfile
		config = SafeConfigParser()
		config.read('../server-sleep.cfg')
		self.checkinterval = int(config.get('serverSleep', 'checkinterval'))
		self.sleepcmd = config.get('serverSleep', 'sleepcmd')
		self.enabledmodules = eval(config.get('serverSleep', 'enabledmodules'))
		self.modules = None
		self.logger = log()
		
		for enabledmodule in self.enabledmodules:
			self.modules.append(__import__(enabledmodule))
		
	def __del__(self):
		pass
	
	def startup (self):
		while True:	
			self.logger.logger.log ("Wait " + str(self.general_checkinterval) + " secs...")
			time.sleep(self.general_checkinterval)
			
			self.logger.log ("Checks started")
			for enabledmodule in self.enabledmodules
				status = self.modules.[enabledmodule].run()
				if status == 1:
					continue
				elif status == 2:
					break
				elif status ==  -1:
					self.logger.log (enabledmodule + "failed!", 1)

			self.logger.log("All Checks OK: Going to Sleep Now!", 3, True)
			os.system(self.sleepcmd);
			self.logger.log("Sleep is over: Server woke up!", 3, True)