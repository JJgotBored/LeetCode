class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        n = len(prices)

        value1 = [0 for i in range(n)]
        value2 = [0 for i in range(n)]
        for i in range(n):
            value1[i] =  prices[i] - prices[0] - fee

        value1[0]= 0

        for i in range(1,n):
            value2[i] = max(0, value1[i])
            for j in range(i,n):
                value2[j] = value2[i] + prices[j] - prices[i] - fee
                value2[j] = max(value2[j], value2[j-1], value1[j])
            value1 = value2[:] 
        
        #print(value1)
        #print(value2)
        return value2[n-1]
    
def main():
    prices = [1,3,2,8,4,9]
    #prices = [1,3,7,5,10,3]
    fee = 2
    test = Solution()
    print(test.maxProfit(prices, fee))

if(__name__ == "__main__"):
    main()