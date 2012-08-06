How to register a checkmodul
============================
Run `server-sleep --configure` as root

How to build own checkmodul
===========================
-	Create a new .py file.
-	Name it what ever you want (e.g. examplecheck.py)
-	Create a Class in it with the same name! (e.g. class examplecheck(object))
-	Implement a staticmethod which name have to be run
	-	return values have to be:
		0 -> conditions ok for going to sleep
		1 -> don't sleep
		2 -> go to sleep, no matter whar other checks say
		-1 -> an error occurred
-	implemnt a static method configure() which contains configfile information
-	a staticmethod called info() which returns a short description would be nice
	
If you need an example look 3 lines below or at one of the existing checks. pingcheck.py should be a simple one...
Happy coding ;-)

Example checkmodul
====================
You find this example in the additional folder.
Please don't copy the lines below. Trust me, you won't be happy!

<code>
example.py

	#!/usr/bin/env python
	#-*- coding: utf-8 -*-
	
	import sys, os
	from ConfigParser import SafeConfigParser
	
	sys.path.append("../classes/")
	from log import log
	
	class example(object):
		"""
	Write what your check do here!
		"""
		def __init__(self):
			# Read Configfile
			config = SafeConfigParser()
			config.read('check-modules/example.cfg')
			
			# add your iptions here like this:
			self.option  = int(config.get('example', 'option'))
			self.option2  = int(config.get('example', 'option2'))
			
			self.logger = log()
			
		def __del__(self):
			pass
		
		def check(self):
			try:
				# do your check stuff here
				
				# things you need:
				#
				# retrun 0 -> don't go to sleep. here is something to wait for
				# return 1 -> ready for sleep
				# retrun 2 -> go to sleep, no matter what other checks say
				# retrun -1 -> an error occurred
				#
				# self.logger.log("Example: Message")    -> print info to logfile
				# self.logger.log("Example: Message", 2) -> print warning to logfile
				# self.logger.log("Example: Message", 1) -> print error to logfile
				return 0
			except:
				return -1
		
		@staticmethod
		def run():
			instance = example()
			instance.logger.log("Example: check started")
			return instance.check()
		
		@staticmethod
		def configure():
			configurable = []
			# add the configfile option you used here also
			# configurable.append([sectionname, optionname, defaultvalue, description])
			configurable.append(["example", "option", '0', "an example option"])
			configurable.append(["example", "option2", '-1', "just another option"])
			return configurable
	
	
	# for testing purpose
	# if you run "python example.py" the important functions will be executed
	if __name__ == '__main__':
		os.chdir('../')
		print example.run()
		print example.configure()
		print example.__doc__
</code>