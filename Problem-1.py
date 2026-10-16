# Python If-Else

# https://www.hackerrank.com/challenges/py-if-else/problem

#Task
#Given an integer, , perform the following conditional actions:

#If n is odd, print Weird
#If n is even and in the inclusive range of  to , print Not Weird
#If n is even and in the inclusive range of  to , print Weird
#If n is even and greater than , print Not Weird

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    
    if n%2!=0:
        print("Weird")
    else:
        if 2<=n<=5:
            print("Not Weird")
        elif 6<=n<=20:
            print("Weird")
        elif n>20:
            print("Not Weird")
