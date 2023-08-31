#LeetCode Problem: Product of Array Except Self

#

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [1] * (len(nums)) #result array is size of nums + 1

        prefix = 1
        for i in range(len(nums)): #for each element in nums
            result[i] = prefix #result array indice = prefix
            prefix *= nums[i] #prefix multiplied by itself and the current nums indice

        postfix = 1
        for i in range(len(nums) - 1, -1, -1): #starting at the end of nums to the beginning
            result[i] *= postfix #multiply postfix by the value at the indice of teh result array
            postfix *= nums[i] #multiply postfix by whatever number is at the nums indice
        return result   #return result array

