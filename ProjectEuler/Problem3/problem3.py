#Solution for the problem no-3
#Find the largest prime factor of our input
#  Eg:- largest prime factor of 13195 among  5,7,13,29 is 29

import logging

def largest_pfactor(n):
    i = 2
    while i * i < n:
        while n % i == 0:
            n = n / i
        i = i + 1
    return n

def main ():
    logging.basicConfig(filename='problem3.log',level=logging.INFO)
    max = raw_input("Program to find the largest prime factor from a range:\nEnter the max range:")
    if max.isdigit():
        result = largest_pfactor(int(max))
        logging.info("Largest prime factor from " + max + " is " + str(result))
        print "result",result
    else:
        logging.error("Invalid max range: " + max + " \nUsage: Integer value only ")
        print "Invalid max range: " + max + " \nUsage: Integer value only "

if __name__ == '__main__':
    main()

