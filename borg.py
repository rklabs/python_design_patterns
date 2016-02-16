'''
    Borq is similar to singleton design pattern, but the main
    difference is use of shared state which results in all object
    references sharing same state. Object comparison will return False.
'''
class Borg(object):
    _shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Borg, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj

borgMe = Borg()
borgU = Borg()
borgMe._attr = 10

print("borgMe._attr %d" % borgMe._attr)
print("borgU._attr %d" % borgU._attr)

print("borgMe is borgU %r" % (borgMe is borgU))

class ChildBorg(Borg):
    pass

borgChild = ChildBorg()

print("borgChild is borgMe %r" % (borgChild is borgMe))
print('borgChild._attr %d' % borgChild._attr)
