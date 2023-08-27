#NeetCode LeetCode #1: TwoSum

#Use hash map to check for difference value, 
#map will add index of last occurance of num. Don't use same element twice

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """  
        hashMap = {} #val : index

        #Enumerate counts the number of iterable items
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashMap: #if number needed to add to the sum is in the hash map
                return [hashMap[diff], i] #return the indices of the nubmers that add to the sum
            hashMap[n] = i
        return
