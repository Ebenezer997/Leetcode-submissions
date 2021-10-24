class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #if array is empty return zero
        if not prices: return 0
        
        #initializing profits and minimum price
        profit = 0
        mini = prices[0]
        #looping through the array(list of prices)
        for i in range(len(prices)):
            #if the next price is lesser than the minimum 
            if prices[i] < mini:
                #interchange it
                mini = prices[i]
            #else we compare the current profit with the previous profit
            else:
                profit = max(profit,prices[i]-mini)
        #return maximum profit when it ends
        return profit
            
       