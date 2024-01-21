#Prime naiev approch
def prime(a):
    if a==1:
        return True
    for i in range (2,a):
        if (a%i==0):
            return False
    return True
a=int(input())
print(prime(a))
    