[![Build Status](https://travis-ci.org/SLCoding/server-sleep.svg?branch=master)](https://travis-ci.org/SLCoding/server-sleep?branch=master)
[![Coverage Status](https://coveralls.io/repos/github/SLCoding/server-sleep/badge.svg?branch=master)](https://coveralls.io/github/SLCoding/server-sleep?branch=master)
[![Requirements Status](https://requires.io/github/SLCoding/server-sleep/requirements.svg?branch=master)](https://requires.io/github/SLCoding/server-sleep/requirements/?branch=master)

## Work in Progress Disclaimer
This project is not ready yet! If you want to use it, please wait until its ready. At this moment you won't have much fun with this dev, pre alpha aka. not working correctly(but on my machine it did) right now version.

# server-sleep

server-sleep is suspends your media server when it's not in use.
This results in lower energy costs and (hopefully) extended hardware life.
Its written in Python 3

There are a bunch of conditions you can choose to check the state.
-	Are local or ssh users logged in?
-	Are computers in the network running?
-	Are processes running which shouldn't be interrupted?
- 	... or what ever you want server-sleep to check. Check out our PluginInterface.


## Why we developed this
If you've got some good ideas to improve this project [let us know](https://github.com/SLCoding/server-sleep-coreplugins/issues/new) or send a PR.

## License
[See License](LICENSE)