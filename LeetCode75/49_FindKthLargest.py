import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        queue = []

        for i in nums:
            heapq.heappush(queue, i)
            if(len(queue) > k):
                heapq.heappop(queue)
        return queue[0]
    
def main():
    #nums = [3,2,1,5,6,4]
    #k = 2
    nums = [3,2,3,1,2,4,5,5,6]
    k = 4
    test = Solution()
    print(test.findKthLargest(nums, k))

if(__name__ == "__main__"):
    main()