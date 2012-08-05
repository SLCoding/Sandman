#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
	This program is free software; you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation; either version 3 of the License,
	or (at your option) any later version.

	This program is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
	See the GNU General Public License for more details.

	You should have received a copy of the GNU General Public License
	along with this program; if not, see <http://www.gnu.org/licenses/>.

	Get more info at: https://github.com/SLCoding/server-sleep

	@author: wiesendaniel (Daniel Wiesendorf)
	@author: Japortie (Marcus Schütte)
	@version: v0.1
"""
import time
from time import gmtime, strftime
import re
import subprocess
from ConfigParser import SafeConfigParser

class serverSleep(object):
	def __init__(self):
		# Read Configfile
		config = SafeConfigParser()
		config.read('server-sleep.cfg')
		self.logging = int(config.get('general', 'logging'))
 		self.checkinterval = int(int(config.get('general', 'checkinterval')))
		self.sleepcmd = config.get('general', 'sleepcmd')
		
	def __del__(self):
		pass
		
	@staticmethod
	def log (self, message, type_ = 3, importand = False):
		# isset workaround; in case of static usage there will be no self.general_debug...
		try:
			logging = self.general_logging
		except NameError:
			config = SafeConfigParser()
			config.read('server-sleep.cfg')
			logging= int(config.get('general', 'logging'))
			
		if (type_ <= logging) or (logging!= 0 and importand == True):
			type_str = None;
			if type_ == 1:
				type_str =  " ERROR: "
			elif type_ == 2:
				type_str =  " WARNING: "
			elif type_ == 3:
				type_str =  " INFO: "
			else:
				type_str =  " UNKNOWN: "
			
			print strftime("%Y-%m-%d %H:%M:%S", gmtime())+type_str+message
			return True
		else:
			return False
	
	def func_sleep (self):
		self.log("All Checks OK: Going to Sleep Now!", 3, True)
		#os.system(self.general_sleepcmd);
		self.log("Sleep is over: Server woke up!", 3, True)
	
	def func_doCheck (self):
		while True:	
			self.log ("Wait " + str(self.general_checkinterval) + " secs...")
			time.sleep(self.general_checkinterval)
			
			self.log ("Checks started")
			
			if self.general_critprocess == True:
				self.log ("Checking for Critical Processes")
				if self.func_critprocess() == False:
					continue
			else:
				self.log("Skip Checking for Critical Processes")

			
			self.log("All Checks OK: Going to Sleep Now!", 3, True)
			self.func_sleep()
			self.log("Sleep is over: Server woke up!", 3, True)
			

# Startup
if __name__ == '__main__':
	instance = serverSleep()
	instance.log("server-sleep started", 3, True)
	serverSleep.log("test", 3, True)
	#instance.func_doCheck()
	instance.log("server-sleep terminated", 3, True)