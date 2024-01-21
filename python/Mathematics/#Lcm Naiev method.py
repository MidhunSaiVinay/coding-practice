#Lcm Naiev method
def lcm(a,b):

    c=max(a,b)
    while True:
        if(c%a==0) and (c%b==0):
            return c
        else:
            c+=1
    return c
a=int(input())
b=int(input())
print(lcm(a,b))
            

