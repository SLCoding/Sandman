from abc import ABC, abstractmethod
from enum import Enum


class AbstractCheckPlugin(ABC):

    """Initialize your Plugin Class"""
    @abstractmethod
    def __init__(self):
        pass

    """Check if the device should go to Sleep"""
    @abstractmethod
    def check(self):
        pass

    # TODO should optional methods as "hooks" raising an exeption?

    """Hock before the check starts"""
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

    # TODO maybe return an Configuration Object, see CheckResult.py?
    """Returns a list of configurable values for the plugin"""
    @abstractmethod
    def configurables(self):
        pass


# TODO move in separate file
class CheckReturn(Enum):
    SLEEP_READY = 1
    DONT_SLEEP = 2
    FORCE_SLEEP = 3
    UNKNOWN = 9


# TODO I don't get it. Please write a comment explaining this
class Configurable(object):

    def ___init___(self, identifier, displayname, examplevalue, description):
        self.identifier = identifier
        self.display_name = displayname
        self.example_value = examplevalue
        self.description = description
