#count of digits in factorial
import math

def digitsInFactorial(N):
    fact=0
    for i in range(1,N+1):
        fact+=(math.log10(i) )
    return math.floor(fact)+1
N=int(input())
print(digitsInFactorial(N))