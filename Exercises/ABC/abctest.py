# sample program for abstract method
from abc import ABCMeta, abstractmethod
class Animal:
    __metaclass__ = ABCMeta

    @abstractmethod
    def say_something(self):
          return "I'm an animal!"
	  pass
class Cat(Animal):
    def say_something(self):
        #s = super(Cat, self).say_something()
	s = "Bibin"
        return "%s - %s" % (s, "Miauuu")

c = Cat()
a = Animal()
a.say_something()
print c.say_something()
