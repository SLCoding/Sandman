### Work In Progress Disclaimer

This project is not ready yet! In fact we just rebooted this project. And this time we do it right! Right?
If you want to use it, do yourself a favor and wait until it's ready. At this moment you won't have much fun with this dev, pre alpha aka. not working correctly(but on my machine it did) right now version. ;-)


# server-sleep

Build:

[![Build Status](https://travis-ci.org/SLCoding/server-sleep.svg)](https://travis-ci.org/SLCoding/server-sleep)

Code Quality:

[![Code Climate](https://codeclimate.com/github/SLCoding/server-sleep/badges/gpa.svg)](https://codeclimate.com/github/SLCoding/server-sleep)
[![Issue Count](https://codeclimate.com/github/SLCoding/server-sleep/badges/issue_count.svg)](https://codeclimate.com/github/SLCoding/server-sleep)
[![Test Coverage](https://codeclimate.com/github/SLCoding/server-sleep/badges/coverage.svg)](https://codeclimate.com/github/SLCoding/server-sleep/coverage)
[![Coverage Status](https://coveralls.io/repos/github/SLCoding/server-sleep/badge.svg)](https://coveralls.io/github/SLCoding/server-sleep)

Dependencies:

[![Requirements Status](https://requires.io/github/SLCoding/server-sleep/requirements.svg)](https://requires.io/github/SLCoding/server-sleep/requirements/)


## Description

server-sleep, you guessed it, puts your server to sleep when it's not in use.
It's aimed towards home/media servers, but in theory you could it use for every linux box you don't want to run 24/7.
This (hopefully) results in lower energy costs and extended hardware life.

There are a bunch of conditions you can choose to check the state.
- Are local or ssh users logged in?
- Are computers in the network running?
- Are processes running which shouldn't be interrupted?
- ... or what ever you want server-sleep to check. Check out our PluginInterface.


## Wanna help us out?

If you've got some good ideas to improve this project [let us know](https://github.com/SLCoding/server-sleep-coreplugins/issues/new) or send a PR.
We don't want you to buy us beer. If you like this project, spread the word.


## License

[See License](LICENSE)