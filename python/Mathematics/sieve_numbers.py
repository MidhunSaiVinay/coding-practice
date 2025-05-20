#sieve numbers
def sieve(n):
    if n<=1:
        return
    isprime =[True]*(n+1)
    i=2
    while i*i<=n:
        if isprime[i]:
            for j in range(i*i,n+1,i):
                isprime[j]=False
        i+=1
    for i in range(2,n+1):
        if isprime[i]:
            print(i,end=" ")
n=int(input())
sieve(n)