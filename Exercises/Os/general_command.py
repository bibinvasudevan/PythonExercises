import os

print os.path.abspath('abspath.py')  # /home/bibin/projects/python/abspath.py
#print os.system('ps -aux')   # Same as we run the pas -aux command in terminal . The output will display in the terminal
			     # We cannot store the output of os.system() to any variable
os.system('ping google.com')

f = os.popen('date')		# If we want to store the commands output to a file then we can use popen function. It will give a object
data = f.read()
print data
