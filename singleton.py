'''
    Singleton design pattern allows creation of single object which
    exists throughout the litetime of the program. Only one object is
    created no matter how many times singleton object is instantiated.
    Object comparison results in True.
'''
class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

singleMe = Singleton()
singleU = Singleton()
singleMe.instance._attr = 10

print("singleMe._attr %d" % singleMe._attr)
print("singleMe is singleU %r" % (singleMe is singleU))

class ChildS(Singleton):
    pass

singleChild = ChildS()

print("singleChild is singleU %r" % (singleChild is singleU))

print("singleChild.instance._attr %r" % singleChild.instance._attr)

