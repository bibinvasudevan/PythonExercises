#    Closure is just a fancy name for a function that remembers the values from the enclosing lexical scope even when the program flow is no longer in the enclosing scope.
#   If you've ever written a function that returned another function, you may have used closures. 
 

def foo():
   x = 3
   def bar():
      print x
   x = 5
   return bar

bar = foo()
bar()   # print 5
	# PLEASE NOTE HOW THE BAR() IS CALLING


# Another Example

def makeConstantAdder(x):
    constant = x
    def adder(y):
        return y + constant
    return adder
 
f = makeConstantAdder(12)
print f(3) #15
g = makeConstantAdder(4)
print g(3)	#7

