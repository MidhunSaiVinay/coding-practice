#Palindrome number
n= int(input())
def palindrome(n):
    rev=0
    temp=n
    while temp>0:
        ld=temp%10
        rev=rev*10+ld
        temp =temp//10
    return rev==n
res=palindrome(n)
print(res)
