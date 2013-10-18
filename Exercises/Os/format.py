# To specify the usage of format

sub1 = "python string!"
sub2 = "an arg"

a = "i am a %s"%sub1
b = "i am a {0}".format(sub1)

c = "with %(kwarg)s!"%{'kwarg':sub2}
d = "with {kwarg}!".format(kwarg=sub2)

print a
print b
print c
print d

ss = "[{0},{1},{2}]".format(1,2,3)
print ss
