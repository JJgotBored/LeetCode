class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        minCost = [1000]*n

        for i in range(n):
            if(i < 2):
                minCost[i] = cost[i]
            else:
                minCost[i] = min(minCost[i-1], minCost[i-2]) + cost[i]

        #print(minCost)
        return min(minCost[n-1], minCost[n-2])
    
def main():
    #cost = [10,15,20]
    cost = [1,100,1,1,1,100,1,1,100,1]
    test = Solution()
    print(test.minCostClimbingStairs(cost))
if(__name__ == "__main__"):
    main()