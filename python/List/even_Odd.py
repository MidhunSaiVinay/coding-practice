#even odd list
n=eval(input())
def EvenOdd(n):
    Even=[]
    Odd=[]
    for i in n:
        if i%2==0:
            Even.append(i)
        else:
            Odd.append(i)
    return Even,Odd
print(EvenOdd(n))
