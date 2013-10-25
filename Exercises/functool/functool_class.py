import functools

class MyClass(object):
    """Demonstration class for functools"""
    
    def meth1(self, a, b=2):
        """Docstring for meth1()."""
        print '\tcalled meth1 with:', (self, a, b)
        return
    
o = MyClass()


o.meth1('no default for a', b=3)
print

p1 = functools.partial(o.meth1, b=4)
#functools.update_wrapper(p1, o.meth1)

p1('a goes here')
print
