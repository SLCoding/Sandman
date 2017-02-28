**Build status**

master:
[![Build Status](https://travis-ci.org/SLCoding/server-sleep.svg?branch=master)](https://travis-ci.org/SLCoding/server-sleep)
develop:
[![Build Status](https://travis-ci.org/SLCoding/server-sleep.svg?branch=develop)](https://travis-ci.org/SLCoding/server-sleep)

TODO: Rewrite this!
Please Wait!
============
This project is not ready yet! If you want to use it, please wait until its ready. At this moment you won't have much fun with this dev version.

server-sleep
============
server-sleep is a script that suspends your homeserver when it's not in use. This results in lower energy costs and extended hardware life.
There are a bunch of conditions you can choose to check the state.
-	Are local or ssh users logged in?
-	Are computers in the network running?
-	Is pyLoad downloading?
-	Are processes running which shouldn't be interruptet?
- 	...

You can choose which of these conditions will be checked.

Installation
============
Its tested on Ubuntu 12.04 and Debian Squeeze.

Requirements
------------
The installation script will check for requirements. We recommend to install all to enable the full range of features
-	python	(Hey, its written in python… you need it!)
-	...

Using the install script
------------------------
-	Download the last stable version or make a clone of this repo
-	run the install.sh as root
-	now configure it by editing / or running "server-sleep --configure"
-	reboot or run "sudo /etc/init.d/server-sleep start"

Hand made installation
----------------------
-	also not ready yet...

Why we developed this
=====================
We coded this for our personal needs. Some members of our team have home servers and don't want them to run 24/7. So, we did this. ;-)
If you've got some good idea to improve this project let us know o,r fork it and code it by yourself. Who knows, maybe your idea is awesome enough for us to include it in our awesome project. ;)

License
=======
[See License](LICENSE)