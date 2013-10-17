class Pizza(object):
    def get_radius(self):
        raise NotImplementedError

class Derived(Pizza):
    def	get_radius(self):
	print "Hello Pizza"

d = Derived()
d.get_radius()

p = Pizza()
p.get_radius()
