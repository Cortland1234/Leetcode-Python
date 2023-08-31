#LeetCode Problem: Contains Duplicate

#Use hashmap to get unique values and to check for duplicates

class Solution(object):
    def containsDuplicate(self, nums):
        hashMap = set() #Create a hash Set for unique numbers 

        for x in nums:
            if x in hashMap: #if number is already in hash set, return True
                return True
            hashMap.add(x) #if not in hash set, add number
        return False #if no duplicates, return False