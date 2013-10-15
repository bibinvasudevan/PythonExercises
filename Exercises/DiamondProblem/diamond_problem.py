# In the following situation diamond problem is  the order in which the call() is taken
# Initially it will taken as B2,B1,B3 and if we restuctures it will take as itsown
class A:
  def call(self):
    pass
 
class B1(A):
  def call(self):
    print "I am parent B1"
 
class B2(A):
  def call(self):
    print "I am parent B2"
 
class B3(A):
  def call(self):
    print "I am parent B3"
 
class C(A):
  def call(self):
    print "I (C) was not invited"
 
class ME(B2, B1, B3):
  def whichCall(self):
    print self.call()
 
  def restructure(self, parent1, parent2, parent3):
    self.__class__.__bases__ = (parent1, parent2, parent3, )
 
  def printBaseClasses(self):
    print self.__class__.__bases__

me = ME()
me.printBaseClasses()
me.whichCall()

me.restructure(B3,B2,B1)
me.printBaseClasses()
me.whichCall()


