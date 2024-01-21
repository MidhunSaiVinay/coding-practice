#Prime Factorization

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
n= int(input())
a= n
def product_of_list(factors):
    result = 1
    for num in factors:
        result *= num
    return result
factors=[]
def PF(n):
    i=2
    
    while i<=n:
        if (prime(i)) and (n%i==0):
            n= n//i
            factors.append(i)
            if product_of_list(factors)==a:
                return print(factors)
        else:
            i+=1
    return a
PF(n)




