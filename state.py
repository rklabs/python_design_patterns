class Implementation1(object):
    def func1(self):
        print "Implementation1 func1"

    def func2(self):
        print "Implementation1 func2"

    def func3(self):
        print "Implementation1 func3"

class Implementation2(object):
    def func1(self):
        print "Implementation2 func1"

    def func2(self):
        print "Implementation2 func2"

    def func3(self):
        print "Implementation2 func3"

class State(object):
    def __init__(self, imp):
        self.__impl = imp

    def changeImpl(self, newImpl):
        self.__impl = newImpl

    def __getattr__(self, name):
        return getattr(self.__impl, name)

def runner(obj):
    obj.func1()
    obj.func2()
    obj.func3()

app = State(Implementation1())
runner(app)
app.changeImpl(Implementation2())
runner(app)
