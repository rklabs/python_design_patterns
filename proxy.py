class Implementation(object):
    def func1(self):
        print "Implementation of func1"

    def func2(self):
        print "Implementation of func2"

    def func3(self):
        print "Implementation of func3"

class Proxy():
    def __init__(self):
        self.__implementation = Implementation()

    def func1(self):
        self.__implementation.func1()

    def func2(self):
        self.__implementation.func2()

    def func3(self):
        self.__implementation.func3()

p = Proxy()

p.func1()
p.func2()
p.func2()


