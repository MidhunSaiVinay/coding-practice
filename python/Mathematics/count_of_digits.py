# count of digits
n=int(input())
def count_of_digits(n):
    a=0
    while n>0:
        n=n//10
        a+=1
    return a
res= count_of_digits(n)
print(res)