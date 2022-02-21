# -*- coding: utf-8 -*-
"""
Created on Mon May 17 23:11:53 2021

@author: Administrator
"""


# def fib(n, k):
#     a = 0
#     b = 1
#     for i in range (3, n):
#         c = a + b*k
#         a = b
#         b = c
#         print(c)

# n = 5
# k = 3
# fib(n, k)

def Rabbit(n,k):
    import numpy as np
    P = np.zeros(n)
    P[0] = 1
    P[1] = 1
    P[2] = P[0]*k + P[1]
    for i in range(3, n):
        P[i] = P[i-1] + P[i-2]*k
    
    return P

print(Rabbit(10,2))
