
def sum(x, y):
     def do_it():
             return x + y
     return do_it
 

s =   sum(1, 3)
print s()
