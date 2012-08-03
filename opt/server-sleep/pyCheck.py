import subprocess
import re
CheckString = "No downloads running"


cmd = "pyLoadCli status"
ps = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)

output = ps.stdout.read()
ps.stdout.close()
ps.wait()

if (re.match(CheckString, output)):
	print True
else:
	print False