#Return second largest element
n=eval(input())
def sl(n):
    if len(n)<=1:
        return None
    lar=n[0]
    slar=None
    for x in n[1:]:
        if x>lar:
            lar=x
        elif x!=lar:
            if slar==None or slar<x:
                slar=x
    return slar
print(sl(n))
