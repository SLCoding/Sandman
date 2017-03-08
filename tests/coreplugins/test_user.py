# source: http://doc.pytest.org/en/latest/
from serversleep.coreplugins.usercheck import UsercheckPlugin
from serversleep.coreplugins.usercheck import UserInformationUtil
from serversleep.api.PluginInterface import CheckReturn
import unittest
from unittest.mock import MagicMock


class UserPluginTest(unittest.TestCase):

    def test_create_usercheckplugin(self):
        configurations = {
            "max_usr": 3,
            "max_usr_local": 2,
            "max_usr_remote": 2,
            "idle_timeout": 3600
        }
        user_check_plugin = UsercheckPlugin(configurations)
        self.assertEquals(user_check_plugin.max_usr, 3)
        self.assertEquals(user_check_plugin.max_usr_local, 2)
        self.assertEquals(user_check_plugin.max_usr_remote, 2)
        self.assertEquals(user_check_plugin.idle_timeout, 3600)

    def test_returns_sleep_ready(self):
        configurations = {
            "max_usr": 3,
            "max_usr_local": 2,
            "max_usr_remote": 2,
            "idle_timeout": 3600
        }
        user_check_plugin = UsercheckPlugin(configurations)
        mocked_user_util = UserInformationUtil()
        mocked_user_util.get_local_session_count = MagicMock(return_value=1)
        mocked_user_util.get_remote_session_count = MagicMock(return_value=1)
        mocked_user_util.get_session_count = MagicMock(return_value=2)
        user_check_plugin._user_information_util = mocked_user_util

        self.assertEquals(user_check_plugin.check(), CheckReturn.SLEEP_READY)

    def test_exceed_max_usr(self):
        configurations = {
            "max_usr": 3,
            "max_usr_local": 3,
            "max_usr_remote": 3,
            "idle_timeout": 3600
        }
        user_check_plugin = UsercheckPlugin(configurations)
        mocked_user_util = UserInformationUtil()
        mocked_user_util.get_local_session_count = MagicMock(return_value=2)
        mocked_user_util.get_remote_session_count = MagicMock(return_value=2)
        mocked_user_util.get_session_count = MagicMock(return_value=4)
        user_check_plugin._user_information_util = mocked_user_util

        self.assertEquals(user_check_plugin.check(), CheckReturn.DONT_SLEEP)

    def test_exceed_max_local(self):
        configurations = {
            "max_usr": 5,
            "max_usr_local": 1,
            "max_usr_remote": 4,
            "idle_timeout": 3600
        }
        user_check_plugin = UsercheckPlugin(configurations)
        mocked_user_util = UserInformationUtil()
        mocked_user_util.get_local_session_count = MagicMock(return_value=2)
        mocked_user_util.get_remote_session_count = MagicMock(return_value=2)
        mocked_user_util.get_session_count = MagicMock(return_value=4)
        user_check_plugin._user_information_util = mocked_user_util

        self.assertEquals(user_check_plugin.check(), CheckReturn.DONT_SLEEP)

    def test_exceed_max_remote(self):
        configurations = {
            "max_usr": 5,
            "max_usr_local": 4,
            "max_usr_remote": 1,
            "idle_timeout": 3600
        }
        user_check_plugin = UsercheckPlugin(configurations)
        mocked_user_util = UserInformationUtil()
        mocked_user_util.get_local_session_count = MagicMock(return_value=2)
        mocked_user_util.get_remote_session_count = MagicMock(return_value=2)
        mocked_user_util.get_session_count = MagicMock(return_value=4)
        user_check_plugin._user_information_util = mocked_user_util

        self.assertEquals(user_check_plugin.check(), CheckReturn.DONT_SLEEP)
