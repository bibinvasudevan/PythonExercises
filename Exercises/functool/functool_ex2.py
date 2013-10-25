import functools

def myfunc(a, b=2):
    """Docstring for myfunc()."""
    print '\tcalled myfunc with:', (a, b)
    return





p1 = functools.partial(myfunc, b=4)


print 'Updating wrapper:'
print '\tassign:', functools.WRAPPER_ASSIGNMENTS
print '\tupdate:', functools.WRAPPER_UPDATES
print

functools.update_wrapper(p1, myfunc)

