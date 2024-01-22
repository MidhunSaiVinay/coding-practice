#modulo inverse
a=int(input())
m=int(input())
def modInverse(a,m):
    for i in range(1,m+1):
        if (i*a)%m==1:
            return i
    return -1
print(modInverse(a,m))