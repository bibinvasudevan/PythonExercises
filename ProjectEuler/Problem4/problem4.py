# Program to find out the largest palindrom made from n digit number
# Eg: 9009 = 91*99

import logging

def palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False

def largest_palindrom(min, max):
    i = min
    j = min
    greatest = 0
    while (i <= max):
        while (j <= max):
            product = i * j
            if (product > greatest and palindrome(str(product))):
                greatest = product
            j += 1
        j = min
        i += 1
    return str(greatest)

def main ():
    logging.basicConfig(filename='problem4.log',level=logging.INFO)
    min = raw_input("Program to find the largest palindrom from n digit number(Usage eg: 100,999):\nEnter the min range:")
    max = raw_input("Enter the max range:")
    if max.isdigit() and min.isdigit():
        result = largest_palindrom(int(min),int(max))
        logging.info("Largest palindrom is " + str(result))
        print "result",result
    else:
        logging.error("Invalid max range: " + max + " \nUsage: Integer value only ")
        print "Invalid max range: " + max + " \nUsage: Integer value only "

if __name__ == '__main__':
    main()

