#!/bin/python3

import math
import os
import random
import re
import sys

def insertionSort1(n, arr):
    right=n-1
    num=arr[n-1]
    for i in range(n):
        while right >=0:
            if num<arr[right-1] and right!=0:
                arr[right]=arr[right-1]
                right -=1
                print(*arr)
            else:
                break
    arr[right]=num
    print(*arr)
            
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
