#! /usr/bin/env

import math

"""
Every positive fraction can be represented as sum of unique unit fractions.
A fraction is unit fraction if numerator is 1 and denominator is a positive integer,
for example 1/3 is a unit fraction. Such a representation is called Egyptial Fraction as it was used by ancient Egyptians.

Following are few examples:
Egyptian Fraction Representation of 2/3 is 1/2 + 1/6
Egyptian Fraction Representation of 6/14 is 1/3 + 1/11 + 1/231
Egyptian Fraction Representation of 12/13 is 1/2 + 1/3 + 1/12 + 1/156
"""


def printEgyptian(numerator, denominator):
    fractions = []
    if numerator == 1:
        return "1/" + str(denominator)

    if denominator % numerator == 0:
        return "1/" + str(denominator/numerator)

    while True:
        de = (denominator + numerator - 1) / numerator
        fractions.append("1/" + str(de))
        numerator = numerator * de - denominator
        denominator = denominator * de
        if numerator == 1:
            fractions.append("1/" + str(denominator))
            break
        
        if denominator % numerator == 0:
            fractions.append("1/" + str(denominator/numerator))
            break
    
    return "+".join(fractions)

if __name__ == "__main__":
    print printEgyptian(2, 3)
    print printEgyptian(6, 14)
    print printEgyptian(12, 13)
