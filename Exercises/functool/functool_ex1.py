import functools

def myfunc(a, b=2):
    """Docstring for myfunc()."""
    print '\tcalled myfunc with:', (a, b)
    return




myfunc('a', 3)
print

p1 = functools.partial(myfunc, b=4)

p1('default a')
p1('override b', b=5)
print

p2 = functools.partial(myfunc, 'default a', b=99)

p2()
p2(b='override b')
print

print 'Insufficient arguments:'
p1()
