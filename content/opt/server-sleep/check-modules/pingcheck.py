from ConfigParser import SafeConfigParser
import subprocess

class pingcheck(object):
	def __init__(self):
		# Read Configfile
		config = SafeConfigParser()
		config.read('pingcheck.cfg')
		self.hostlist = eval(config.get('pingcheck', 'hostlist'), {}, {})
		self.max_hosts = int(config.get('pingcheck', 'max_hosts'))
		
	def __del__(self):
		pass
	
	def check(self):
		try:
			count = 0;
			for host in self.hostlist:
				ret = subprocess.call("ping -c 2 %s" % host,
					shell=True,
					stdout=open('/dev/null', 'w'),
					stderr=subprocess.STDOUT
				)
				if ret == 0:
					serverSleep.log("Pingcheck: Host "+ ip +" is up!")
					count += 1
					if count>self.max_hosts:
						serverSleep.log("Pingcheck: Not Ready for sleep! More hosts active then allowed!", 2)
						return 0
				else:
					serverSleep.log("Pingcheck: Host "+ ip +" is down!")
					
			serverSleep.log("Pingcheck: Ready for sleep!")
			return 1
		except:
			return -1
	
	@staticmethod
	def run(self):
		serverSleep.log ("Pingcheck: check started")
		instance = pingcheck()
		return instance.check()
	
	@staticmethod
	def configure(self)
		pass
	
	@staticmethod
	def info(self)
		infostr "check for computers in your network which are running"
		retrun infostr