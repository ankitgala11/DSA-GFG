#User function Template for python3

class Solution:
    def assignMiceHoles(self, N , M , H):
        # code here
        
        M.sort()
        H.sort()
        
        ans=0
        
        
        for i in range(N):
            
            ans = max(ans,  abs( M[i] - H[i]) )
            
            
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        M=list(map(int,input().split()))
        H=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.assignMiceHoles(N,M,H))
# } Driver Code Ends