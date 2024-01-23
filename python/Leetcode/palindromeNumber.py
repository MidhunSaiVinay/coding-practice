def isPalindrome( x: int) -> bool:
        temp=x
        rev=0
        while temp>0:
            ld=temp%10
            rev=rev*10+ld
            temp=temp//10
        return x==rev
x=int(input())
print(isPalindrome( x))