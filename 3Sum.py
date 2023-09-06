#Leetcode: 3Sum

#sort the input array

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [] #result will return a list of lists of triplets

        nums.sort() #sort the input array

        for i, a in enumerate(nums): #iterate through the index and the values
            if i > 0 and a == nums[i - 1]: #if the value is reused 
                continue

            left, right = i + 1, len(nums) - 1 #solve twoSum using left and right pointers
            while left < right:
                threeSum = a + nums[left] + nums[right] #if left < right, the value plus the left and right pointer = threeSum
                if threeSum > 0: #if threeSum is more than 0, decrement the right pointer
                    right -= 1
                elif threeSum < 0: #if threeSum is less than 0, increment the left pointer
                    left += 1
                else:
                    result.append([a, nums[left], nums[right]]) #else, append the sum to the results list

                    left += 1
                    while nums[left] == nums[left - 1] and left < right: #if left == left - 1, then it is the same value. You need to shift the pointer again to get a different value
                        left += 1

        return result        
