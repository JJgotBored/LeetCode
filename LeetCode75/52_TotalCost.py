class Solution:
    def totalCost(self, costs: list[int], k: int, candidates: int) -> int:

        pairs = []

        for i in range(len(costs)):
            pairs.append([costs[i], i])

        #pairs.sort(reverse = True)

        return 0
    
def main():
    costs = [17,12,10,2,7,2,11,20,8]
    k = 3
    test = Solution()

if(__name__ == "__main__"):
    main()
        