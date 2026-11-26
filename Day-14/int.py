if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)
    print(a//b)
    print(a/b)





#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getRemovableIndices' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING str1
#  2. STRING str2
#

def getRemovableIndices(str1, str2):
    n, m = len(str1), len(str2)
    if n != m +1:
        return [-1]
    left = 0
    while left < m and str1[left] == str2[left]:
        left += 1
    right = m
    while right > 0 and str1[right] == str2[right -1]:
        right -= 1
    if left < right:
        return [-1]
    return list(range(right, left +1))
    # Write your code here

if __name__ == '__main__':
    str1 = input()

    str2 = input()

    result = getRemovableIndices(str1, str2)

    print('\n'.join(map(str, result)))
    print(get_removable_indices("abdgggda", "abdggda"))
    
