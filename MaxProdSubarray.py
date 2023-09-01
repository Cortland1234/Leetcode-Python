#LeetCode: Maximum Product Subarray


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = max(nums) #initialize result to max of nums
        currentMin, currentMax = 1, 1

        for n in nums:
            if n == 0: #if 0 is encountered in array, reset min and max
                currentMax, currentMin = 1, 1
                continue #continue to next iteration
            
            temp = currentMax * n #keep track of currentMax before it is changed in next line
            currentMax = max(n * currentMax, n * currentMin, n) #set mins and max. These could be n*curMin, n*curMax, or n itself 
            currentMin = min(temp, n * currentMin, n)
            
            result = max(result, currentMax, currentMin)
        return result    