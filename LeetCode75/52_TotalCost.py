import heapq
class Solution:
    def totalCost(self, costs: list[int], k: int, candidates: int) -> int:

        pairs = []
        pool1 = []
        pool2 = []
        l = len(costs)
        curSum = 0
        difCost = 0
        difIndex = 0

        for i in range(l):
            pairs.append([costs[i], i])

        for i in range(candidates):
            if(pairs != []):
                heapq.heappush(pool1, pairs.pop(0))
            if(pairs != []):
                heapq.heappush(pool2, pairs.pop())

        
        #pool1.sort()
        #pool2.sort()
        #pairs.sort(reverse = True)
                
        for i in range(k):
            if(len(pool1) > 0 and len(pool2) > 0):
                difCost = pool1[0][0] - pool2[0][0]
                difIndex = pool1[0][1] - pool2[0][1]

                if(difCost < 0):
                    curSum += pool1[0][0]
                    heapq.heappop(pool1)
                    if(pairs != []):
                        heapq.heappush(pool1, pairs.pop(0))
                elif(difCost > 0):
                    curSum += pool2[0][0]
                    heapq.heappop(pool2)
                    if(pairs != []):
                        heapq.heappush(pool2, pairs.pop())
                elif(difIndex < 0):
                    curSum += pool1[0][0]
                    heapq.heappop(pool1)
                    if(pairs != []):
                        heapq.heappush(pool1, pairs.pop(0))
                else:
                    curSum += pool1[0][0]
                    heapq.heappop(pool1)
                    if(pairs != []):
                        heapq.heappush(pool1, pairs.pop(0))
            elif(len(pool1) > 0):
                curSum += pool1[0][0]
                heapq.heappop(pool1)
            else:
                curSum += pool2[0][0]
                heapq.heappop(pool2)

        print(pool1)
        print(pool2)


        return curSum
    
def main():
    #costs = [17,12,10,2,7,2,11,20,8]
    #k = 3
    #cand = 4

    costs = [1,2,4,1]
    k = 3
    cand = 3
    test = Solution()
    print(test.totalCost(costs, k, cand))

if(__name__ == "__main__"):
    main()
        