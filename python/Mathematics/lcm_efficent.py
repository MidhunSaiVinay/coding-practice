#lcm efficent
def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
def lcm(a,b):
    return a*b//gcd(a,b)

a=int(input())
b=int(input())
print(lcm(a,b))