'''
describe an algoritham that given a set s of n  integers another integer x 
determine weather s contains s contains two elements whoose sum is exactly x in nlogn time
'''
from mergesort import mergeSort1
def twopointer(S,n,x):
    mergeSort1(S,0,n-1)
    left = 0
    right = len(S) - 1
    
    # Step 3: Two-pointer technique
    while left < right:
        current_sum = S[left] + S[right]
        
        if current_sum == x:
            return True
        elif current_sum < x:
            left += 1
        else:
            right -= 1
        print('*')
    
    # Step 4: No pair found
    return False
# S=[1,2,3,4,5,6,7]
# n=len(S)
# x=7
# print(twopointer(S,n,x))