class Solution:
    def tribonacci(self, n: int) -> int:
        memo=[-1]*(n+1)

        def compute_trib(i):
            if i<0:
                return 0
            if memo[i] != -1:
                return memo[i]
            
            if i == 0:
                memo[i]=0
                return 0
            elif i ==1 or n ==2:
                memo[i]=1
                return 1
                
            result=compute_trib(i - 1) + compute_trib(i - 2) + compute_trib(i - 3)
            memo[i]=result
            return result
        return compute_trib(n)

        
        # if n == 0:
        #     return 0
        # elif n==1 or n == 2:
        #     return 1

        # a,b,c=0,1,1
        # for i in range(3, n+1):
        #     d=a+b+c
        #     a,b,c = b,c,d
        # return c