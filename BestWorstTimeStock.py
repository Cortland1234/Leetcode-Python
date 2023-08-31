#Leetcode Problem: Best Time to Buy and Sell Stock

#Two pointers, left pointer behind right

#Variable for current max, "maxP"

#While right pointer is less than the length of prices,
#if left is less than right then the profit is right - left
#maxP = max(maxP, profit) <-- maxP is the maximum number between maxP and profit

#increment right by 1 

class Solution(object):
    def maxProft(self, prices):
        left, right = 0, 1
        maxP = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - profit[left]
                maxP = max(maxP, profit)
            else:
                left = right
            
            right += 1

        return maxP