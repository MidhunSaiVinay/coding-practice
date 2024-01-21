# Divisors of a number naiev method
n= int (input())

def divisors(n):
    for i in range(1,n+1):
        if (n%i==0):
            print(i)
    
divisors(n)


