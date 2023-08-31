#LeetCode Problem: Maximum Subarray

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        maxSub = nums[0] #start at 0 index of nums
        currentSum = 0 #initialize current sum at 0

        for n in nums:
            if currentSum < 0: #if currentSum is ever negative, then set currentSum to 0
                currentSum = 0
            currentSum += n #otherwise, add n to currentSum
            maxSub = max(maxSub, currentSum) #maxSub is either the max of maxSub or currentSub
        return maxSub