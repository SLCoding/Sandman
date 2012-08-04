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
		self.general_checkuser = bool(int(config.get('general', 'checkuser')))
		self.general_checkip = bool(int(config.get('general', 'checkip')))
		self.general_checkpyload = bool(int(config.get('general', 'checkpyload')))
		self.general_critprocess = bool(int(config.get('general', 'critprocess')))
		self.general_checkinterval = int(int(config.get('general', 'checkinterval')))
		self.general_sleepcmd = config.get('general', 'sleepcmd')
		self.user_max_usr  = int(config.get('user', 'max_usr'))
		self.user_max_usr_local  = int(config.get('user', 'max_usr_local'))
		self.user_max_usr_remote  = int(config.get('user', 'max_usr_remote'))
		self.user_idle_timeout = int(config.get('user', 'idle_timeout'))
		self.checkip_ip_addr = eval(config.get('checkip', 'ip_addr'), {}, {})
		self.checkip_max_hosts = int(config.get('checkip', 'max_hosts'))
		self.critprocess_processnames = eval(config.get('critprocess', 'processnames'), {}, {})
		self.critprocess_processids = eval(config.get('critprocess', 'processids'), {}, {})
		self.general_debug = int(config.get('general', 'debug'))
		
	def __del__(self):
		pass
	
	def log (self, message, type_ = 3, importand = False):
		if (type_ <= self.general_debug) or (self.general_debug!= 0 and importand == True):
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
	
	def func_checkuser(self):
		max_user = self.user_max_usr
		max_local = self.user_max_usr_local
		max_remote = self.user_max_usr_remote
		idle_timeout = self.user_idle_timeout
		cmd = "w -hs"
		
		
		ps = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
		
		output = ps.stdout.read()
		ps.stdout.close()
		ps.wait()
			
		user = 0
		local_user = 0
		remote_user = 0
		
		i = 0
		for line in output.split("\n"):
			
			if(line != "" and line != None):
				self.log("Proccessing User " + str(i))
				fields = line.split()
				
				if(len(fields) < 5):
					idle = fields[2]
					location = ":--"
				else:
					idle = fields[3]
					location = fields[2]
					
				idle_time = 0
				
				hours = 0
				minutes = 0
				seconds = 0
				
				if(re.match("^[0-9]+\:[0-9]+m$", idle)):
					#hours:minutes
					idle = idle.split(":")
					hours = int(idle[0])
					minutes = int(idle[1].replace("m", ""))
					
				elif(re.match("^[0-9]+\.[0-9]+s$", idle)):
					#second.microsecond
					idle = idle.split(".")
					seconds = int(idle[0])
					
				elif(re.match("^[0-9]+\:[0-9]+$", idle)):
					#minutes:seconds
					idle = idle.split(":")
					minutes = int(idle[0])
					seconds = int(idle[1])
				else:
					self.log("User " + str(i) + " Idle time couldn't be parsed!", 2)
					
				idle_time = (hours * 60 + minutes) * 60 + seconds
				self.log("User " + str(i) + " Idle Time = " + str(idle_time) + " secs")
				local = False
				
				if (re.match("^\:.*$", location)):
					local = True
					
				if(idle_time < idle_timeout or idle_timeout < 0):
					user += 1
					if(local):
						self.log("User " + str(i) + " Location: Local")
						local_user += 1
					else:
						self.log("User " + str(i) + " Location: Remote")
						remote_user += 1
				i += 1
		
		self.log("Users: " + str(i))
		self.log("Active: " + str(user))
		self.log("Inactive: " + str(i-user))
		self.log("Local: " + str(local_user))
		self.log("Remote: " + str(remote_user))
		
		if((max_user < user and max_user >=0) or (max_local < local_user and max_local >= 0) or (max_remote < remote_user and max_remote >= 0)):
			self.log("User: Not Ready for sleep! More users active then allowed!", 2)
			return False
		
		self.log("User: Ready for sleep!")
		return True
	
	def func_checkip(self):
		count = 0;
		for ip in self.checkip_ip_addr:
			ret = subprocess.call("ping -c 2 %s" % ip,
				shell=True,
				stdout=open('/dev/null', 'w'),
				stderr=subprocess.STDOUT
			)
			if ret == 0:
				self.log("CheckIP: Host "+ ip +" is up!")
				count += 1
				if count>self.checkip_max_hosts:
					self.log("CheckIP: Not Ready for sleep! More hosts active then allowed!", 2)
					return False
			else:
				self.log("CheckIP: Host "+ ip +" is down!")
				
		self.log("CheckIP: Ready for sleep!")
		return True
			
	def func_checkpyload(self):
		CheckString = "No downloads running"
		cmd = "pyLoadCli status"
		ps = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
		
		output = ps.stdout.read()
		ps.stdout.close()
		ps.wait()
		
		if (re.match(CheckString, output)):
			self.log("pyLoad: Ready for sleep!")
			return True
		else:
			self.log("pyLoad: Not Ready for sleep! Downloads still active!", 2)
			return False
			
	def func_critprocess_check(self, proc, id = 0):
		ps = subprocess.Popen("ps -A", shell=True, stdout=subprocess.PIPE)
		ps_pid = ps.pid
		output = ps.stdout.read()
		ps.stdout.close()
		ps.wait()
	
		for line in output.split("\n"):
			if line != "" and line != None:
				fields = line.split()
				pid = fields[0]
				pname = fields[3]
				if(id == 0):
					if(pname == proc):
						self.log("Process '" + proc +"' is still active!", 2)
						return True
				else:
					if(pid == proc):
						self.log("Process '" + proc +"' is still active!", 2)
						return True
							
		return False
	
	def func_critprocess(self):
		for processname in self.critprocess_processnames:
			self.log("Checking process with name: " + processname)
			if self.func_critprocess_check(processname) == True:
				self.log("CritProcess: Not Ready for sleep! Critical Process '" + processname + "' still active!", 2)
				return False
				
		for processid in self.critprocess_processids:
			self.log("Checking process with id: " + processid)
			if self.func_critprocess_check(processid, 1) == True:
				self.log("CritProcess: Not Ready for sleep! Critical Process '" + processid + "'  still active!", 2)
				return False
				
		self.log("CritProcess: Ready for sleep!")
		return True
	
	def func_sleep (self):
		pass
		#os.system(self.general_sleepcmd);
	
	def func_doCheck (self):
		while True:	
			self.log ("Wait " + str(self.general_checkinterval) + " secs...")
			time.sleep(self.general_checkinterval)
			
			self.log ("Check started")
			
			if self.general_critprocess == True:
				self.log ("Checking for Critical Processes")
				if self.func_critprocess() == False:
					continue
			else:
				self.log("Skip Checking for Critical Processes")
				
				
			if self.general_checkuser == True:
				self.log ("Checking for Users logged in")
				if self.func_checkuser() == False:
					continue
			else:
				self.log("Skip Checking for Users logged in")
				
				
			if self.general_checkpyload == True:
				self.log ("Checking for PyLoad status")
				if self.func_checkpyload() == False:
					continue
			else:
				self.log("Skip Checking for PyLoad status")
				
				
			if self.general_checkip == True:
				self.log ("Checking for network machines")
				if self.func_checkip() == False:
					continue
			else:
				self.log("Skip Checking for network machines")
			
			self.log("All Checks OK: Going to Sleep Now!", 3, True)
			self.func_sleep()
			self.log("Sleep is over: Server woke up!", 3, True)
			

# Startup
instance = serverSleep()
instance.log("server-sleep started")
instance.func_doCheck()