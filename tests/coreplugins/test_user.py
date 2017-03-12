# source: http://doc.pytest.org/en/latest/
from sandman.coreplugins.usercheck import UsercheckPlugin
from sandman.coreplugins.usercheck import UserInformationUtil
from sandman.api.PluginInterface import CheckReturn
import unittest
from mock import MagicMock


class UserPluginTest(unittest.TestCase):

    @staticmethod
    def get_configuration():
        return {
            "max_usr": 3,
            "max_usr_local": 2,
            "max_usr_remote": 2,
            "idle_timeout": 3600
        }

    def test_create_usercheckplugin(self):
        user_check_plugin = UsercheckPlugin(UserPluginTest.get_configuration())
        self.assertEquals(user_check_plugin.max_usr, 3)
        self.assertEquals(user_check_plugin.max_usr_local, 2)
        self.assertEquals(user_check_plugin.max_usr_remote, 2)
        self.assertEquals(user_check_plugin.idle_timeout, 3600)

    def test_get_configurables(self):
        configurables = UsercheckPlugin.configurables()
        self.assertEquals(len(configurables), 4)

    def test_returns_sleep_ready(self):
        user_check_plugin = UsercheckPlugin(UserPluginTest.get_configuration())
        mocked_user_util = UserInformationUtil()
        mocked_user_util.get_local_session_count = MagicMock(return_value=1)
        mocked_user_util.get_remote_session_count = MagicMock(return_value=1)
        mocked_user_util.get_session_count = MagicMock(return_value=2)
        user_check_plugin._user_information_util = mocked_user_util

        self.assertEquals(user_check_plugin.check(), CheckReturn.SLEEP_READY)

    def test_exceed_max_usr(self):
        user_check_plugin = UsercheckPlugin(UserPluginTest.get_configuration())
        mocked_user_util = UserInformationUtil()
        mocked_user_util.get_local_session_count = MagicMock(return_value=2)
        mocked_user_util.get_remote_session_count = MagicMock(return_value=2)
        mocked_user_util.get_session_count = MagicMock(return_value=4)
        user_check_plugin._user_information_util = mocked_user_util

        self.assertEquals(user_check_plugin.check(), CheckReturn.DONT_SLEEP)

    def test_exceed_max_local(self):
        user_check_plugin = UsercheckPlugin(UserPluginTest.get_configuration())
        mocked_user_util = UserInformationUtil()
        mocked_user_util.get_local_session_count = MagicMock(return_value=3)
        mocked_user_util.get_remote_session_count = MagicMock(return_value=0)
        mocked_user_util.get_session_count = MagicMock(return_value=3)
        user_check_plugin._user_information_util = mocked_user_util

        self.assertEquals(user_check_plugin.check(), CheckReturn.DONT_SLEEP)

    def test_exceed_max_remote(self):
        user_check_plugin = UsercheckPlugin(UserPluginTest.get_configuration())
        mocked_user_util = UserInformationUtil()
        mocked_user_util.get_local_session_count = MagicMock(return_value=0)
        mocked_user_util.get_remote_session_count = MagicMock(return_value=3)
        mocked_user_util.get_session_count = MagicMock(return_value=0)
        user_check_plugin._user_information_util = mocked_user_util

        self.assertEquals(user_check_plugin.check(), CheckReturn.DONT_SLEEP)
