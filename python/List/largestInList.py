#largest number in list
n=eval(input())
def largest(n):
    l=1
    for i in n:
        if i>l:
            l=i
    return l
print(largest(n))
