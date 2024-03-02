import heapq

class Solution:

    def maxScore(self, nums1: list[int], nums2: list[int], k: int) -> int:
        l = len(nums1)
        pairs = []
        subset = []
        curSum = 0
        curMin = 1000001
        answer = -1

        for i in range(l):
            pairs.append([nums2[i], nums1[i]])  
        pairs.sort(reverse = True)
        #print(pairs)
        
        heapq.heapify(subset)

        #fills queue to size k 
        for i in range(k):
            heapq.heappush(subset, pairs[i][1])
            curSum += pairs[i][1]
            curMin = min(curMin, pairs[i][0])
        
        answer = max(answer, curSum * curMin)

        for i in range(k, l):
            #print(i)
            temp = heapq.heappop(subset)
            curSum -= temp

            heapq.heappush(subset, pairs[i][1])
            curMin = min(curMin, pairs[i][0])
            curSum += pairs[i][1]

            answer = max(answer, curSum*curMin)
          
        #print(subset)
        return answer


def main():
    nums1 = [1,3,3,2]
    nums2 = [2,1,3,4]
    k = 3
    #nums1 = [4,2,3,1,1]
    #nums2 = [7,5,10,9,6]
    #k = 1
    #nums1 = [22,5,25,15,28,1]
    #nums2 = [22,30,25,25,9,18]
    #k = 3
    test = Solution()
    print(test.maxScore(nums1, nums2, k))

if(__name__ == "__main__"):
    main()