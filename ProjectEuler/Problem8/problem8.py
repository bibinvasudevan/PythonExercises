# Program to find the greatest product of five consecutive digits in the
# 1000-digit number.

import logging


def max_pro5digit(longNum):
    tempProd = 0
    maxProd = 0

    for i in range(0, len(longNum) - 5):
        tempProd = int(longNum[i]) * int(longNum[i + 1]) * int(
            longNum[i + 2]) * int(longNum[i + 3]) * int(longNum[i + 4])
        if tempProd > maxProd:
            maxProd = tempProd
    return maxProd


def main():
    logging.basicConfig(filename='problem8.log', level=logging.INFO)
    max = raw_input(
        "Enter the bigdigit number to find the greatest product of 5 consequttive digit:")
    if max.isdigit():
        result = max_pro5digit(max)
        logging.info("The greatest product is  " + str(result))
        print "The product is", result
    else:
        logging.error(
            "Invalid number: " + max + " \nUsage: Integer value only ")
        print "Invalid number: " + max + " \nUsage: Integer value only "

if __name__ == '__main__':
    main()
