#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys
from ConfigParser import SafeConfigParser
import subprocess
sys.path.append("../classes/")
from log import log

class pyloadcheck(object):
	"""
check if pyLoad is currently downloading
	"""
	def __init__(self):
		# Read Configfile
		config = SafeConfigParser()
		config.read('pyloadcheck.cfg')
		self.path = str(config.get('pyloadcheck', 'path'))
		self.logger = log()
		
	def __del__(self):
		pass
	
	def check(self):
		try:
			CheckExprs = ("No downloads running", "Could not establish")
			
			cmd = "pyLoadCli status"
			ps = subprocess.Popen(path + cmd, shell=True, stdout=subprocess.PIPE)
			
			output = ps.stdout.read()
			ps.stdout.close()
			ps.wait()
			for Expr in CheckExprs:
				if (re.match(CheckString, output)):
					self.log("pyLoad: Ready for sleep!")
					return 0
			return 1
		except:
			return -1
	
	@staticmethod
	def run():
		instance = pyloadcheck()
		instance.logger.log ("pyLoad Check: check started")
		return instance.check()
	
	@staticmethod
	def configure():
		configurable = []
		configurable.append(["pyloadcheck", "path", "/usr/bin/", "path where the pyLoad binaries are stored"])
		return configurable


# for testing purpose
if __name__ == '__main__':
	os.chdir('../')
	print pingcheck.run()
	print pingcheck.configure()
	print pingcheck.__doc__
	