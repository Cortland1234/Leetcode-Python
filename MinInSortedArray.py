#LeetCode: Find Minimum in Rotated Sorted Array

#binary search with a middle pointer. if the middle pointer is greater than
#or equal to the left pointer, then search right. otherwise search left
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curResult = nums[0]

        left, right = 0, len(nums) -1 #left is at 0, right is at the last element in nums

        while left <= right:
            if nums[left] < nums[right]: #if the array is sorted and left is less than right
                curResult = min(curResult, nums[left]) #then result is the min of either curResult or left
                break

            middle = (left + right) // 2 #middle pointer is the left and right pointer divided by 2 (integer division for whole number)
            curResult = min(curResult, nums[middle]) #set the result to the min of itself or the middle pointer
            if nums[middle] >= nums[left]: #if middle is greater than or equal to the left, the middle pointer is part of the left side of the array
                left = middle + 1 #search the right side of the array by doing middle + 1
            else:
                right = middle - 1 #if on the right side of the array, do the opposite (middle - 1)
        
        return curResult