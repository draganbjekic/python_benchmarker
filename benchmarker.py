""" random time intensive program"""

import timeit

def sum_a_lot_of_numbers(number=50000000):
    """ function to be run by timeit"""
    sum_total = 0
    while number > 0:
        sum_total = sum_total + 1
        number = number - 1

print(timeit.Timer(sum_a_lot_of_numbers).timeit(number=15)/15)
