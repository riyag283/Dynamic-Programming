# Range Sum Query - Immutable
'''
Question: Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.
'''
# A brute force approach would be to loop through elements from i to j
# To speed up the calculation, we have take have to caching

class NumArray:

    def __init__(self, nums: List[int]):
        self.dp = nums
        for i in range(1, len(nums)):
            self.dp[i] += self.dp[i-1]

    def sumRange(self, i: int, j: int) -> int:
        return self.dp[j] - self.dp[i-1] if i else self.dp[j]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
