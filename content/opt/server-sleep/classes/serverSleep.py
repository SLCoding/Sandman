#!/usr/bin/env python
#-*- coding: utf-8 -*-
import sys, os, time

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
			module = __import__(enabledmodule,  globals(), locals(), [enabledmodule], -1)
			self.modules.append(module)
			
		print self.modules
		print self.enabledmodules
		
	def __del__(self):
		pass
	
	def startup (self):
		while True:	
			self.logger.log ("Wait " + str(self.checkinterval) + " seconds...")
			time.sleep(self.checkinterval)
			
			self.logger.log ("Checks started")
			#print locals()
			
# 			i = 0
# 			for module in self.modules:
# 				checkclass = locals()[module[self.enabledmodules[i]]]
				
# 				status = module.checkclass.run()
# 				i += 1
# 				if status == 1:
# 					continue
# 				elif status == 2:
# 					break
# 				elif status ==  -1:
# 					self.logger.log (enabledmodule + "failed!", 1)

			self.logger.log("All Checks OK: Going to Sleep Now!", 3, True)
			os.system(self.sleepcmd);
			self.logger.log("Sleep is over: Server woke up!", 3, True)