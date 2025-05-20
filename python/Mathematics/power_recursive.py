#power recursive
n=int(input())
x=int(input())

def power(x,n):
    if n==0:
        return 1
    temp=power(x,n//2)
    temp*=temp
    if n%2==0:
        return temp
    else:
        return temp*x
res=power(n,x)
print(res)