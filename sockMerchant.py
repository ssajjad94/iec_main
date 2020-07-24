# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 12:30:19 2020

@author: 15856
"""


#!/bin/python3


# Complete the sockMerchant function below.
def sockMerchant(n, ar):

    b = {}
    for n in ar:
        # get(key, default) falls back to default if key is not present
        b[n] = b.get(n, 0) + 1
        
    x = 0
    y = 0

    for key, value in b.items():
        # print(key,value, sep=':')
        pairs = value/2
        pairs = int(pairs)
        
        for v in range(pairs):
            x += 1
        odd = value % 2
        for w in range(odd):
            y += 1
            
        #print(key, int(pairs), odd)
        
    print("pairs: ", x)
    print("odds: ", y)
    
    return x

if __name__ == '__main__':

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)
