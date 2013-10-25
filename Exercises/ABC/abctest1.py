# sample program for abstract method
from abc import ABCMeta, abstractmethod

import abc
 
class Animal(object):
    __metaclass__  = abc.ABCMeta
 
    @abc.abstractmethod
    def get_radius(self):
         """Method that should do something."""
	 pass


class Cat(Animal):
    def say_something(self):
        return "%s - %s" % (s, "Miauuu")

c = Cat()
print c.say_something()
