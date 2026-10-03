class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        i = 1
        c = prices[0]
        p = 0

        while i < len(prices):
            cp = prices[i] - c

            if cp < 0: # lost was made, new value is smaller
                c = prices[i]

            elif cp > p: # new value is provide's larger profile, new profit
                p = cp

            print(c, cp, p, prices[i])
            i+=1

        return p