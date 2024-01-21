#GCD navie method
def GCD(a,b):
    c= min(a,b)
    
    for i in range(c,0,-1):
        if (a%i==0) & (b%i==0):
            return i
    
    return a*b     
a=int(input())
b=int(input())
print(GCD(a,b))
