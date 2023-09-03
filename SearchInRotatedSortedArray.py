#Leetcode problem: Search in Rotated Sorted Array

class Solution(object):
    def findTarget(self, nums, target):
        """
        :type nums: List[int]
        :rtype: int
        """

        l, r = 0, len(nums) - 1

        while l <= r: #if target is the middle pointer, return middle
            middle = (l + r) // 2
            if target == nums[middle]:
                return middle
            
            #if we are in the left sorted portion
            if nums[l] <= nums[middle]: #if the left pointer is less than the middle pointer, then we are in the left sorted portion
                if target > nums[middle] or target < nums[l]:
                    l = middle + 1
                else:
                    r = middle - 1
            #if we are in the right sorted portion
            else:
                if target < nums[middle] or target > nums[r]:
                    r = middle - 1
                else:
                    l = middle + 1

        return -1
