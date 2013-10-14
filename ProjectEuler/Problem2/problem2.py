# Solution for the problem no-2
# Program to find out the sum of even value fibanocci series
import logging

def even_fib_sum(limit):
    a,b,sum = 0,1,0
    while a <= int(limit):
        if a%2 == 0:
            sum += a
        a,b = b,a+b
    return sum

def main ():
    logging.basicConfig(filename='problem2.log',level=logging.INFO)
    max = raw_input("Program to find the sum of even fibanoci upto a range:\nEnter the max range:")
    if max.isdigit():
        result = even_fib_sum(max)
        logging.info("The sum of even fibanoci in " + max + " is " + str(result))
        print "result",result
    else:
        logging.error("Invalid max range: " + max + " \nUsage: Integer value only ")
        print "Invalid max range: " + max + " \nUsage: Integer value only "

if __name__ == '__main__':
    main()

