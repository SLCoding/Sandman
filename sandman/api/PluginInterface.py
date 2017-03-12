from abc import abstractmethod, ABCMeta
from enum import Enum


class AbstractCheckPlugin():
    __metaclass__ = ABCMeta
    """Initialize your Plugin Class"""
    @abstractmethod
    def __init__(self):
        pass

    """Check if the device should go to Sleep"""
    @abstractmethod
    def check(self):
        pass

    """Hook before the check starts"""
    def pre_check(self):
        raise NotImplementedError

    """Hook after the check is finished"""
    def post_check(self):
        raise NotImplementedError

    """Hook before device is going to sleep"""
    def pre_sleep(self):
        raise NotImplementedError

    """Hook after the device is woken up"""
    def post_sleep(self):
        raise NotImplementedError

    """Returns a list of configurable values for the plugin"""
    @abstractmethod
    def configurables(self):
        pass


class CheckReturn(Enum):
    SLEEP_READY = 1
    DONT_SLEEP = 2
    FORCE_SLEEP = 3
    UNKNOWN = 9


class Configurable(object):

    def __init__(self, identifier, displayname, examplevalue, description):
        self.identifier = identifier
        self.display_name = displayname
        self.example_value = examplevalue
        self.description = description
