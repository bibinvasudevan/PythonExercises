# Solution for the problem no-1
# Program to find the sum of the multiple of 3,5 in a range

import logging

def sum_multiple35(max):
    result = 0
    for i in range(0, int(max)):
        if i%3 == 0 or i%5 == 0:
            result = result + i
    return result

def main ():
    logging.basicConfig(filename='problem1.log',level=logging.INFO)
    max = raw_input("Program to find the sum of multiple of 3,5:\nEnter the max range:")
    if max.isdigit():
        sum = sum_multiple35(max)
        logging.info("The sum of multiple of 3,5 in " + max + " is " + str(sum))
        print "sum",sum
    else:
        logging.error("Invalid max range: " + max + " \nUsage: Integer value only ")
        print "Invalid max range: " + max + " \nUsage: Integer value only "

if __name__ == '__main__':
    main()

