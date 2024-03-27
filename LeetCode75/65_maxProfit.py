class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        n = len(prices)

        value = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            value[0][i] =  prices[i] - prices[0] - fee

        value[0][0] = 0

        for i in range(1,n):
            value[i][i] = max(0, value[i-1][i])
            for j in range(i,n):
                value[i][j] = value[i][i] + prices[j] - prices[i] - fee
                value[i][j] = max(value[i][j], value[i][j-1], value[i-1][j]) 
        
        #print(prices)
        #print(value)

        return value[n-1][n-1]
    
def main():
    #prices = [1,3,2,8,4,9]
    prices = [1,3,7,5,10,3]
    fee = 3
    test = Solution()
    print(test.maxProfit(prices, fee))

if(__name__ == "__main__"):
    main()