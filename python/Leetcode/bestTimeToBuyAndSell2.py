class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Returns maximum profit that can be obtained by buying and selling stocks
        
        Solution 1 (Valley-Peak approach):
        - Find local valleys and peaks
        - Add difference between each peak and valley
        Time: O(n), Space: O(1)
        
        Solution 2 (Cumulative differences approach):
        - Add all positive price differences between consecutive days
        Time: O(n), Space: O(1) 
        """
        # Solution 2 is cleaner and more efficient
        maxprofit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                maxprofit += prices[i] - prices[i-1]
        return maxprofit