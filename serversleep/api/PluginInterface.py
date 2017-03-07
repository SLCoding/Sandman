from abc import ABC, abstractmethod, ABCMeta
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

    """Perform tasks that should be done before the device is set to sleep"""
    def pre_sleep(self):
        raise NotImplementedError

    """Perform tasks that should be done after wake up"""
    def post_sleep(self):
        raise NotImplementedError

    """Return a list of Configurable values for the Plugin"""
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
