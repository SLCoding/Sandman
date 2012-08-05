#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys
#import getopt
from ConfigParser import SafeConfigParser
import subprocess
sys.path.append("../classes/")
from log import log

class usercheck(object):
	"""
check for users which are logged in
	"""
	def __init__(self):
		# Read Configfile
# 		config = SafeConfigParser()
# 		config.read('usercheck.cfg')
# 		self.hostlist = eval(config.get('usercheck', 'hostlist'), {}, {})
# 		self.max_hosts = int(config.get('usercheck', 'max_hosts'))
		self.logger = log()
		
	def __del__(self):
		pass
	
	def check(self):
		try:
			return 0
		except:
			return -1
	
	@staticmethod
	def run():
		instance = usercheck()
		instance.logger.log ("Usercheck: check started")
		return instance.check()
	
	@staticmethod
	def configure():
		configurable = ("pingcheck", "hostlist", '("hostname","192.168.0.1")', "list of ip-addresses or hostnames to check")
		configurable.append("pingcheck", "max_hosts", '0', "maximal amount of network devices allowed for putting the machine to sleep")
		return configurable


# for testing purpose
if __name__ == '__main__':
	print usercheck.run()
	print usercheck.configure()
	print usercheck.__doc__