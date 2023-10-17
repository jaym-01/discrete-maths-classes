import numpy as np
import sys

def fLastTwo(n):

    a = 1
    b = 1
    
    for i in range(2, n):
        a, b = b, a+b
    
    return b

def fAnalytical(n):
    phi = (1 + np.sqrt(5))/ 2

    num = pow(phi, n) - pow((1 - phi), n)

    ans = np.round(num/np.sqrt(5))

    return ans

# 
# 11
# 01
# 

def fMatrix(n):

    M = np.array([
        [1, 1],
        [1, 0]
    ])




out = []
for i in range(1, 101):
    out.append(fMatrix[i]);