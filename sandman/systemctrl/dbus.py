from pydbus import SessionBus

# TODO I'm not happy with the naming of this module. -> Find a better name
# TODO check for privileges to suspend

bus = SessionBus()
power = bus.get('org.freedesktop.UPower', '/org/freedesktop/UPower')


def suspend():
    power.Suspend()


def hibernate():
    power.Hibernate()


if __name__ == '__main__':
    suspend()

