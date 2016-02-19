import abc

class ApplicationFramework(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self.__template_method()

    def __template_method(self):
        self.customize1()
        self.customize2()

    @abc.abstractmethod
    def customize1(self):
        pass

    @abc.abstractmethod
    def customize2(self):
        pass

class MyApp(ApplicationFramework):
    def customize1(self):
        print "customize1"

    def customize2(self):
        print "customize2"

MyApp()
