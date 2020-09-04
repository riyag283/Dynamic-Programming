# Recursive formula for Fibonacci: fib(n) = fib(n-1) + fib(n-2)

# Bottom-up Approach
def fib(n, F):
    if F[n] < 0:
        if n==0:
            F[n] = 0
        elif n==1:
            F[n] = 1
        else:
            F[n] =  fib(n-1, F) + fib(n-2, F)
      
    return F[n]

n = int(input())
F = [-1] * (n+1)
print(fib(n, F))
