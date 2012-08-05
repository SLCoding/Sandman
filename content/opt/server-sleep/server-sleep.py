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

Get more information at: https://github.com/SLCoding/server-sleep

@author: wiesendaniel (Daniel Wiesendorf)
@author: Japortie (Marcus Schütte)
@version: v0.1
"""

import os, sys
import getopt

sys.path.append("classes/")
from log import log
from serverSleep import serverSleep


class Usage(Exception):
	def __init__(self, msg):
		self.msg = msg

def main(argv=None):
	"""
	usage: server-sleep [-h] [--help]
	                    [-u] [--usage]
	                    [-s] [--start]
	                    [-c] [--configure]
	                    [-l] [--log]
	"""
	if not os.geteuid()==0:
		sys.exit("Only root can run this script")
		
	if argv is None:
		argv = sys.argv
	try:
		try:
			opts, args = getopt.getopt(argv[1:], "huscl", ["help", "usage", "start", "configure", "log"])
		except getopt.error, msg:
			raise Usage(msg)
		
		# option processing; breaks are written because only the first option is important
		for option, value in opts:
			if option in ("-h", "--help"):
				print __doc__
				break
				
			elif option in ("-u", "--usage"):
				print self.__doc__
				break
				
			elif option in ("-s", "--start"):
				instance = serverSleep()
				instance.log("server-sleep started", 3, True)
				instance.startup()
				instance.log("server-sleep terminated", 3, True)
				break
				
			elif option in ("-c", "--configure"):
				print "configure"
				break
			elif option in ("-l", "--log"):
				print "show logfile..."
				break
			
		return 0

	except Usage, err:
		print str(err.msg)
		print "for help use --help or --usage"
		return 2


if __name__ == "__main__":
	sys.exit(main())