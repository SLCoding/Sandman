#!/usr/bin/env python
#-*- coding: utf-8 -*-

from time import gmtime, strftime
from ConfigParser import SafeConfigParser

class log (object):
	def __init__(self):
		# Read Configfile
		config = SafeConfigParser()
		config.read('../server-sleep.cfg')
		self.mode = int(config.get('log', 'mode'))
		
	def __del__(self):
		pass
		
	def log (self, message, type_ = 3, importand = False):
		if (type_ <= self.mode) or (self.mode!= 0 and importand == True):
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