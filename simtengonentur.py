import numpy as np

def factorial(n):
    result = 1
    if n==0:
        result= 1
    else: 
        for i in np.arange(1,n+1):
            result= result*i
    return result
    
if (factorial(0)==1 & (factorial(1)==1):
    print("No errors")    