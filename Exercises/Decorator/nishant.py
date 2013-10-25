def timer(fn):
    def wrapper(a):
        #Here you can put time stamp for example
        print "Entered function"
        fn(a)
        print "Exiting function"
    return wrapper

@timer
def something(a):
    print a




