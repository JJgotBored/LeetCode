class Solution:
    def totalCost(self, costs: list[int], k: int, candidates: int) -> int:

        pairs = []
        pool1 = []
        pool2 = []
        l = len(costs)

        for i in range(l):
            pairs.append([costs[i], i])

        for i in range(candidates):
            if(pairs != []):
                pool1.append(pairs.pop(0))
            if(pairs != []):
                pool2.append(pairs.pop())

        
        pool1.sort()
        pool2.sort()
        #pairs.sort(reverse = True)

        print(pool1)
        print(pool2)


        return 0
    
def main():
    costs = [17,12,10,2,7,2,11,20,8]
    k = 3
    cand = 4
    test = Solution()
    print(test.totalCost(costs, k, cand))

if(__name__ == "__main__"):
    main()
        