class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        n = len(prices)
        holding = 0

        value = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            value[0][i] =  prices[i] - prices[0] - fee
            value[1][i] =  prices[i] - prices[1] - fee

        value[0][0] = 0
        value[1][0] = 0
        value[1][1] = 0

        #for i in range(n):
        #    for j in range(n):
        #        if(holding == 0):


        print(value)

        return 0
    
def main():
    prices = [1,3,2,8,4,9]
    fee = 2
    test = Solution()
    print(test.maxProfit(prices, fee))

if(__name__ == "__main__"):
    main()