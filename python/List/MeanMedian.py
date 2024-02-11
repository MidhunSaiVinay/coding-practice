def median(self,A,N):
        
        A.sort()
        
        ##Your code here
        #If median is fraction then convert the median to integer and retur
        if N%2==0:
            m1=A[(N//2)-1]
            m2=A[N//2]
            return (m1+m2)//2
        else:
            return A[N//2]
     
    #Function to find mean of the array elements.   
    def mean(self,A,N):
        ##Your code here
        b=0
        for i in A:
            b+=i
        return b//N