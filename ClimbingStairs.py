''' 
Question: You are climbing a stair case. It takes n steps to reach to the top.
          Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''

''' 
Example: given n = 3,
            f[3]
           1/   \2
           /     \
        f[2]     f[1]
        1/ \2    1/ \2
        /   \   [0] [-1]
     f[1]   [0]
     1/ \2
    [0] [-1]
    
For calulating f(x), it's sufficient to calculate f(x-1) and f(x-2),
and once f(x) has been calculated it's efficient to store its value for future use.
The given problem is reduced to Fibonaaci Series, f(n) = f(n-1) + f(n-2)
'''
class Solution:
    # bottom-up
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp = [-1] * (n+1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        
        for i in range(3, n+1):
            dp[i] = dp[i-1] +dp[i-2]
        return dp[n]
