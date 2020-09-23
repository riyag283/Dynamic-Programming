'''
Given 3 numbers {1, 3, 5}, we need to tell
the total number of ways we can form a number 'N' 
using the sum of the given three numbers.
(allowing repetitions and different arrangements).
'''

import timeit

def func(n):
    if n < 1:
        return 0
    if n == 1:
        return 1
    if n == 3:
        return 2
    if n == 5:
        return 5
    return (func(n-1) + func(n-3) + func(n-5))

def dpfunc(n):
    dp = [-1]*(n+1)
    dp[0] = 0
    dp[1] = 1
    dp[2] = 1
    dp[3] = 2
    dp[4] = 3
    dp[5] = 5

    for i in range(6, n+1):
        dp[i] = dp[i-1] + dp[i-3] + dp[i-5]
    return dp[n]

# Driver code
n = int(input())
start = timeit.default_timer()
print(func(n))
stop = timeit.default_timer()
print('Time: ', stop - start)  
print()
start = timeit.default_timer()
print(dpfunc(n))
stop = timeit.default_timer()
print('Time: ', stop - start)  

'''
50
Recursive
3237119305
Time:  638.3213931

Dynamic Programming
3237119305
Time:  0.003923999999983607
'''
