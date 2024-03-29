#User function Template for python3

class Solution:
    ##Complete this function
    # Function to find number of bits needed to be flipped to convert A to B
    def countBitsFlip(self,a,b):
        ##Your code here
        
        cnt=0
        while a and b:
            
            cnt+=(a&1) ^ (b&1)
            a=a>>1
            b=b>>1
            
            
        while a :
            cnt+=a&1
            a=a>>1
            
        while b:
            cnt+=b&1
            b=b>>1
            
            
        return cnt
            
            
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3


import math



def main():
    
    T=int(input())
    
    while(T>0):
        
        
        ab=[int(x) for x in input().strip().split()]
        a=ab[0]
        b=ab[1]
        ob=Solution()
        print(ob.countBitsFlip(a,b))
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends