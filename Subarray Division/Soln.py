#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    sums = 0
    res = 0
    if len(s)==1:
        if d==s[0] and m==1:
            return(1)
        else:
            return(0)
    else:
        for i in range(len(s)):
            sums = s[i]
            count = 1
            for j in range(i+1, len(s)):
                count += 1
                sums = sums+s[j]
                if count==m and sums==d:
                    res+=1
        return res   
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
