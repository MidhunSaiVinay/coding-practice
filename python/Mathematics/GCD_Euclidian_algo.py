# GCD of two nums Euclidian algo
def GCD(a,b):
    while a!=b:
        if a>b:
            a-=b
        else:
            b-=a
    return a
a=int(input())
b=int(input())
print(GCD(a,b))

