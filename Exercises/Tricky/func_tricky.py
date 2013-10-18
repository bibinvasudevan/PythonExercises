mylist = [2,1,4,5,9,12,45]
print map(str,mylist)  # ['2', '1', '4', '5', '9', '12', '45']


#---------------
names = ['Anne', 'Amy', 'Bob', 'David', 'Carrie', 'Barbara', 'Zach']
lengths = map(len, names)
print lengths  # [4, 3, 3, 5, 6, 7, 4]

#--------------------
# lambda usage

print (lambda x, y: x*y)(3, 4) # 12
# or
g = lambda x, y: x*y
print g(10, 10)		#100

#---------------------------

# Map and lambda together

squares = map(lambda x: x**2, range(10))
print squares	# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81

# Other example linking map and filter

square = map(lambda x: x**2 ,range(10))
evensquare = filter(lambda x: x % 2 == 0, square)
print evensquare
