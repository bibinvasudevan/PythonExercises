# SOlution for the problem no-6
# Program to find the difference between the sum of the squares
#  of the first ten natural numbers and the square of the sum 

import logging

def diff_sumsquare(max):
  N = int(max)
  sum1, sum2 = 0, 0
  for i in range(1, N + 1):
    sum1 += i
    sum2 += pow(i,2)
  return pow(sum1,2) - sum2

def main ():
    logging.basicConfig(filename='problem6.log',level=logging.INFO)
    max = raw_input("Program to find the diff of the sum of natural numbers square and their sum's square n:\nEnter the range:")
    if max.isdigit() :
        result = diff_sumsquare(max)
        logging.info("The sum  is " + str(result))
        print "The sum is",result
    else:
        logging.error("Invalid max range: " + max + " \nUsage: Integer value only ")
        print "Invalid max range: " + max + " \nUsage: Integer value only "

if __name__ == '__main__':
    main()
