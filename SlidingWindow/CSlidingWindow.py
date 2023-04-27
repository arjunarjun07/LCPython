from collections import Counter


class CSlidingWindow:
    def maxProfit(self, prices: list[int]) -> int:
        
        maxprofit = 0
        
        if len(prices) == 1:
            return maxprofit
        
        L = 0 
        R = 1
        
        while L < R and L < len(prices) and R < len(prices):                   

            #Selling price is higher than the Cost price. So we have a profit. We are greedy to find further price to check we have more profit. So move only 'R'
            if prices[L] < prices[R]: 
                curr_profit = prices[R] - prices[L]
                maxprofit = max(maxprofit, curr_profit)
            else:
                #Found a new price which is lower than the previous. So jumping "L" to the current location "R". Then continue sliding R till end
                L = R
            R += 1
                
        return maxprofit
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        L = 0
        maxlen = 0
        charset = set()
        
        for R in range(len(s)):
            while s[R] in charset:
                charset.remove(s[L])
                L += 1
            
            charset.add(s[R])
            maxlen = max(maxlen, R - L +1)
                
        return maxlen
    
    def characterReplacement(self, s: str, k: int) -> int:    
        
        maxlen = 0
        L = 0
        chr_freq = {}
        
        for R in range(len(s)):
            chr_freq[s[R]] = 1 +  chr_freq.get(s[R], 0)
            
            while (R - L + 1 - max(chr_freq.values()) > k):
                chr_freq[s[L]] -= 1
                L += 1
            
            maxlen = max(maxlen, R-L+1)
            
        return maxlen    
                
                   
sol = CSlidingWindow()
print(sol.characterReplacement("AABABBA", 1))