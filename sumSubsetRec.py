# Subset Sum Problem
# Recursive solution

'''
Given a set of non-negative integers, and a value sum, 
determine if there is a subset of the given set with sum equal to given sum.
'''

def checkSubset(set,n,sum):
    #base cases
    if sum==0:
        return True
    if (n==0 and sum!=0):
        return False
    
    #if last element is greater than sum
    if set[n-1]>sum:
        return checkSubset(set,n-1,sum)
    #else check if last element can be included in the sum or not
    else:
        return (checkSubset(set,n-1,sum-set[n-1]) or checkSubset(set,n-1,sum))

#driver code
n=int(input("Enter number of elements: "))
set = [int(input("Enter element: ")) for i in range(n)]
sum=int(input("Enter sum: "))
print(set)
if checkSubset(set,n,sum)==True:
    print ("Yes, found.")
else:
    print ("Sorry, not found.")
