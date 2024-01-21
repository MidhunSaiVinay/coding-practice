#Divisors of a number efficent 1
n=int(input())
def Divisors(n):
    i=1
    while (i*i<=n):
        if(n%i==0):
            print (i)
            if (i !=n/i):
                print(n//i)
        i+=1
Divisors(n) 