import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    x=[]
    y=[]
    ar.sort()
    while len(ar)>1:
        if ar[0]==ar[1]:
            x.append(ar[:2])
            del ar[:2]
        else:
            del ar[0]

    return len(x)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
