#lower numbers
n=eval(input())
l=int(input())
m=[]
def lower(n,l):
    
    for i in n:
        if i<l:
            m.append(i)
    return m
print(lower(n,l))
