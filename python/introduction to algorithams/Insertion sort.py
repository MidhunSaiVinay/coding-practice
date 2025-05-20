'''
Insertion sort
Insertion sort sorts array one element at a time key is the element which we sort in the array
kay is selected in for loop and in while loopp we check if key is less than the element before if we move the element
and we check the if key is less than all elements before the key where loop fails we swap key and that element.
 
diffrence between sorting in ascending and descendin order is we just check element is greater than key in while loop
'''
#increasing order
def insertionsort(a,n):
    for i in range(1,n):
        key=a[i]
        j=i-1
        while j>=0 and a[j]>key:
            a[j+1]=a[j]
            j=j-1
        a[j+1]=key
    return a
a=[9,2,5,4]
n=len(a)
print(insertionsort(a,n))
#decreasing order
def dinsertionsort(a,n):
    for i in range(1,n):
        key=a[i]
        j=i-1
        while j>=0 and a[j]<key:
            a[j+1]=a[j]
            j=j-1
        a[j+1]=key
    return a
a=[9,2,5,4]
n=len(a)
print(dinsertionsort(a,n))