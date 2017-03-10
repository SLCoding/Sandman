from enum import Enum


class CheckResult():
    pass
# TODO write me...


class CheckReturn(Enum):
    SLEEP_READY = 1
    DONT_SLEEP = 2
    FORCE_SLEEP = 3
    UNKNOWN = 9
