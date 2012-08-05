How to register a Checkmodul
============================
<<<<<<< HEAD:content/opt/server-sleep/check-modules/README.md
n/a
=======
Simply add a new line with the modulname in the "enabledmoduls" file
Don't forget to restart server-sleep
>>>>>>> dev-japortie:content/opt/server-sleep/check-modules/README

How to build own Checkmodul
===========================
-	Create a new .py file.
-	Name it what ever you want (e.g. 1337check.py)
-	Create a Class in it with the same name! (e.g. class 1337check(object))
-	Implement a staticmethod which name have to be run
	-	return values have to be:
		0 -> don't sleep
		1 -> conditions ok for going to sleep
		2 -> go to sleep, what ever other checks say
		-1 -> an error occurred
-	if you have a config file name it the same as the script with the extension .cfg
	-	implemnt a static method configure() which contains a configuration dialog
-	a staticmethod called info() which returns a short description would be nice
	
You can use "serverSleep.log("message", type)" to print at the logfile... (type: 3=Info; 2=Warning; 1=Error)
	
If you need an example look at ping check. It's a simple one.
Happy coding ;-)