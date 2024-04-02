class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        n = len(prices)

        value1 = -100000
        value2 = 0
        temp = 0

        for i in range(n):
            temp = value1
            value1 = max(value1, value2 - prices[i])
            value2 = max(value2, temp+prices[i] -fee)
        
        return value2
    
def main():
    #prices = [1,3,2,8,4,9]
    prices = [1,3,7,5,10,3]
    fee = 3
    test = Solution()
    print(test.maxProfit(prices, fee))

if(__name__ == "__main__"):
    main()