#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import os
import psutil
import time
from serversleep.api.PluginInterface import AbstractCheckPlugin, CheckReturn, Configurable


class UsercheckPlugin(AbstractCheckPlugin):
    """
check for users which are logged in
    """

    def __init__(self, configuration):
        self.logger = logging.getLogger(__name__)
        self.configuration = configuration

        self.max_usr = self.configuration["max_usr"]
        self.max_usr_local = self.configuration["max_usr_local"]
        self.max_usr_remote = self.configuration["max_usr_remote"]
        self.idle_timeout = self.configuration["idle_timeout"]

        self._user_information_util = UserInformationUtil()

    def __del__(self):
        pass

    def check(self):
        session_counts = self._user_information_util.get_session_counts(self.idle_timeout)

        if self.max_usr >= 0 and session_counts["all"] > self.max_usr:
            self.logger.info("Too many user sessions. Prevent sleep")
            return CheckReturn.DONT_SLEEP
        if self.max_usr_local >= 0 and session_counts["local"] > self.max_usr_local:
            self.logger.info("Too many local user sessions. Prevent sleep")
            return CheckReturn.DONT_SLEEP
        if self.max_usr_remote >= 0 and session_counts["remote"] > self.max_usr_remote:
            self.logger.info("Too many remote user sessions. Prevent sleep")
            return CheckReturn.DONT_SLEEP

        self.logger.info("Ready for sleep")
        return CheckReturn.SLEEP_READY

    @staticmethod
    def configurables():
        return [
                Configurable(
                        "max_usr",
                        "Maximum logged in users",
                        "5",
                        "Specify the maximum number of users that should be ignored when putting the Server to sleep."
                        + " -1 disables check"
                ),
                Configurable(
                        "max_usr_local",
                        "Maximum locally logged in users",
                        "2",
                        "Specify the maximum number of local users that should be"
                        + " ignored when putting the Server to sleep. -1 disables check"
                ),
                Configurable(
                        "max_usr_remote",
                        "Maximum remote logged in users ",
                        "1",
                        "Specify the maximum number of remote users that should be"
                        + " ignored when putting the Server to sleep. -1 disables check"
                ),
                Configurable(
                        "idle_timeout",
                        "User Idle timeout",
                        "3600",
                        "Specify the idle timeout for user sessions. -1 disables timeout"
                )
        ]


class UserInformationUtil:
    def __init__(self):
        self.psutil = psutil

    def get_session_counts(self, idle_timeout):
        sessions = self.psutil.users()
        active_session_counts = {
            "all": 0,
            "local": 0,
            "remote": 0
        }

        for session in sessions:
            idle_time = self.get_idle_time(session.terminal)
            if idle_time <= idle_timeout:
                active_session_counts["all"] += 1
                if self._is_session_remote(session):
                    active_session_counts["remote"] += 1
                else:
                    active_session_counts["local"] += 1

        return active_session_counts

    @staticmethod
    def _is_session_remote(session):
        if session.host != "localhost" and session.host != "127.0.0.1" and session.host != "":
            return True
        else:
            return False

    @staticmethod
    def get_idle_time(terminal):
        if not os.path.isabs(terminal):
            terminal = "/dev/" + terminal
        mod_time = os.path.getmtime(terminal)
        now = time.time()
        return now - mod_time
