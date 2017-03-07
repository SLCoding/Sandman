#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import logging
import psutil
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

    def __del__(self):
        pass

    def check(self):
        sessions = self._get_active_sessions()
        session_count = self._get_session_count(sessions)
        local_session_count = self._get_local_session_count(sessions)
        remote_session_count = self._get_remote_session_count(sessions)

        if session_count > self.max_usr:
            return CheckReturn.DONT_SLEEP
        if local_session_count > self.max_usr_local:
            return CheckReturn.DONT_SLEEP
        if remote_session_count > self.max_usr_remote:
            return CheckReturn.DONT_SLEEP

        return CheckReturn.SLEEP_READY

    def configurables(self):
        configurables = [
                Configurable(
                        "max_usr",
                        "Maximum logged in users",
                        "5",
                        "Specify the maximum number of users that should be ignored when putting the Server to sleep."
                ),
                Configurable(
                        "max_usr_local",
                        "Maximum locally logged in users",
                        "2",
                        """Specify the maximum number of local users that should be
                        ignored when putting the Server to sleep."""
                ),
                Configurable(
                        "max_usr_remote",
                        "Maximum remote logged in users ",
                        "1",
                        "Specify the maximum number of remote users that should be"
                                + " ignored when putting the Server to sleep."
                ),
                Configurable(
                        "idle_timeout",
                        "User Idle timeout",
                        "3600",
                        "Specify the idle timeout for user sessions."
                )
        ]

        return configurables

    def _get_active_sessions(self):
        return psutil.users()

    def _get_session_count(self, sessions):
        active_session_count = 0
        for session in sessions:
            idle_time = self._get_session_idle_time(session)
            if(idle_time <= self.idle_timeout):
                active_session_count += 1

        return active_session_count

    def _get_local_session_count(self, sessions):
        pass

    def _get_remote_session_count(self, sessions):
        pass

    def _get_session_idle_time(self, session):
        pass


# for testing purpose
if __name__ == '__main__':
    os.chdir('../')
    print(usercheck.run())
    print(usercheck.configure())
    print(usercheck.__doc__)
