class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = prices[0]
        Dist = 0
        sum = 0
        for i in prices:
            if min < i:
                sum = i-min
                if Dist<sum:
                    Dist = sum
            elif i<min:
                min = i
            else:
                continue
        return Dist