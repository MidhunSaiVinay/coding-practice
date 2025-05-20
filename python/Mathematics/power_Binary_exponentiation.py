#power iterative Binary exponentiation
import sys
n=int(input())
x=int(input())
def binary(n,x):
    res=1
    while n>0:
        if (n%2 != 0):
            res=res*x
        x=x*x
        n=n//2
    return res
print(binary(n,x))

