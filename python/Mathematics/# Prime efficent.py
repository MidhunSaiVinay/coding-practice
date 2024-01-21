# Prime efficent
def prime(n):
    i=5
    if (n==2) or (n==3):
        return True
    if n==1:
        return False
    if (n%3==0) or (n%2==0):
        return False

    while (i*i <n):
        if (i%n==0):
            return False
        i+=6
    return True
n=int(input())
print(prime(n))