#factorial
N=int(input())
def factorial(N):
    a=1
    for i in range(1,N+1):
        a*=i
    return a
print(factorial(N))