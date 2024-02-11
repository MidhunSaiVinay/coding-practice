#Reverse a list
arr=eval(input())
def reverse(arr):
    return arr[::-1]

def reverse1(arr):
    i=0
    while i<(len(arr)//2):
        arr[i],arr[len(arr)-(i+1)]=arr[len(arr)-(i+1)],arr[i]
        i+=1
    return arr
print(reverse1(arr))
