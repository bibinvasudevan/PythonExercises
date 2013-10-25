def countdown(n):
	if n == 0:
		print "Stoppin the function"
	else:
		print n
		countdown(n-1)

countdown(10)

