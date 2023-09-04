#Leetcode: Palindorme Number

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        
        divider = 1

        while x >= 10 * divider:
            divider *= 10

        while x:
            #to get the right value (the ones place), do x % 10
            r = x % 10
            l = x // divider #to get the hundreds place, divide by 100

            if l != r:
                return False
            
            x = (x % divider) // 10 
            divider = divider / 100 #gets rid of the two l and r values

        return True
