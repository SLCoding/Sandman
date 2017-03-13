# source: http://doc.pytest.org/en/latest/
from serversleep.coreplugins.usercheck import UsercheckPlugin
from serversleep.coreplugins.usercheck import UserInformationUtil
from serversleep.api.PluginInterface import CheckReturn
import unittest
from unittest.mock import MagicMock


class UserPluginTest(unittest.TestCase):

    user_plugin_config = {
        "max_usr": 3,
        "max_usr_local": 2,
        "max_usr_remote": 2,
        "idle_timeout": 3600
    }

    def test_create_usercheckplugin(self):
        user_check_plugin = UsercheckPlugin(UserPluginTest.user_plugin_config)
        self.assertEquals(user_check_plugin.max_usr, 3)
        self.assertEquals(user_check_plugin.max_usr_local, 2)
        self.assertEquals(user_check_plugin.max_usr_remote, 2)
        self.assertEquals(user_check_plugin.idle_timeout, 3600)

    def test_get_configurables(self):
        configurables = UsercheckPlugin.configurables()
        self.assertEquals(len(configurables), 4)

    def test_returns_sleep_ready(self):
        user_check_plugin = UsercheckPlugin(UserPluginTest.user_plugin_config)
        mocked_user_util = UserInformationUtil()
        return_dict = {
            "all": 2,
            "local": 1,
            "remote": 1
        }
        mocked_user_util.get_session_counts = MagicMock(return_value=return_dict)
        user_check_plugin._user_information_util = mocked_user_util

        self.assertEquals(user_check_plugin.check(), CheckReturn.SLEEP_READY)

    def test_exceed_max_usr(self):
        user_check_plugin = UsercheckPlugin(UserPluginTest.user_plugin_config)
        mocked_user_util = UserInformationUtil()
        return_dict = {
            "all": 4,
            "local": 2,
            "remote": 2
        }
        mocked_user_util.get_session_counts = MagicMock(return_value=return_dict)
        user_check_plugin._user_information_util = mocked_user_util

        self.assertEquals(user_check_plugin.check(), CheckReturn.DONT_SLEEP)

    def test_exceed_max_local(self):
        user_check_plugin = UsercheckPlugin(UserPluginTest.user_plugin_config)
        mocked_user_util = UserInformationUtil()
        return_dict = {
            "all": 3,
            "local": 3,
            "remote": 0
        }
        mocked_user_util.get_session_counts = MagicMock(return_value=return_dict)
        user_check_plugin._user_information_util = mocked_user_util

        self.assertEquals(user_check_plugin.check(), CheckReturn.DONT_SLEEP)

    def test_exceed_max_remote(self):
        user_check_plugin = UsercheckPlugin(UserPluginTest.user_plugin_config)
        mocked_user_util = UserInformationUtil()
        return_dict = {
            "all": 3,
            "local": 0,
            "remote": 3
        }
        mocked_user_util.get_session_counts = MagicMock(return_value=return_dict)
        user_check_plugin._user_information_util = mocked_user_util

        self.assertEquals(user_check_plugin.check(), CheckReturn.DONT_SLEEP)
