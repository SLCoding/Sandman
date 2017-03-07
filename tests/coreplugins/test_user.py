# source: http://doc.pytest.org/en/latest/
from serversleep.coreplugins.usercheck import UsercheckPlugin
import unittest


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

