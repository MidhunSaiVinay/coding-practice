#no of digits in factorial
N=int(input())
def digitsInFactorial(N):
    fact=1
    for i in range(1,N+1):
        fact*=i
    return len(str(fact))
print(digitsInFactorial(N))