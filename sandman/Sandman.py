#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, time
import importlib

import configparser
import logging
from sandman.api import PluginInterface


class Sandman(object):

    def __init__(self):
        # Read Configfile
        config = configparser.ConfigParser()
        config.read('server-sleep.cfg')
        self.checkinterval = int(config.get('serverSleep', 'checkinterval'))
        self.sleepcmd = config.get('serverSleep', 'sleepcmd')
        self.enabledmodules = eval(config.get('serverSleep', 'enabledmodules'))
        self.plugins = []
        self.logger = logging.getLogger(__name__)

        for enabledmodule in self.enabledmodules:
            module = importlib.import_module("sandman.coreplugins." + enabledmodule, enabledmodule)
            plugin = getattr(module, enabledmodule)()
            if isinstance(plugin, PluginInterface.AbstractCheckPlugin):
                self.plugins.append(plugin)
                self.logger.info("Module loaded: " + enabledmodule)
            else:
                self.logger.warning("Loaded Module appears to be no CheckPlugin: " + enabledmodule)

    def __del__(self):
        pass

    def startup(self):
        while True:
            self.logger.info("Wait " + str(self.checkinterval) + " seconds...")
            time.sleep(self.checkinterval)

            result = True

            self.logger.info("Checks started")
            status = None
            for plugin in self.plugins:
                plugin_name = plugin.__class__.__name__
                status = plugin.check()

                if status == 1:
                    result = False
                elif status == 2:
                    result = True
                    break
                elif status == -1:
                    self.logger.error(plugin_name + " failed!")

            if not result:
                continue

            self.logger.info("All Checks OK: Going to Sleep Now!")
            for plugin in self.plugins:
                plugin_name = plugin.__class__.__name__
                try:
                    plugin.pre_sleep()
                except NotImplementedError:
                    self.logger.debug("pre_sleep() not implemented in Plugin: " + plugin_name)

            os.system(self.sleepcmd)

            self.logger.info("Sleep is over: Server woke up!")
            for plugin in self.plugins:
                try:
                    plugin.post_sleep()
                except NotImplementedError:
                    self.logger.debug("post_sleep() not implemented in Plugin: " + plugin_name)

