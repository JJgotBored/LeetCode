class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        lQueue = []
        rQueue = []
        lLen = 0
        rLen = 0
        l = len(nums)
        i = 0

        while(i < l):
            if(lLen == 0 and rLen == 0):    # no ints in queue
                lQueue.append(nums[i])
                lLen += 1
                i += 1
            elif(lLen == 0):        # no ints in left queue
                if(rLen >= k): 
                    if(nums[i] > rQueue[rLen -1]):
                        lQueue.append(rQueue.pop())
                        lLen += 1
                        rLen -= 1
                    else:
                        i += 1
                else:
                    if(nums[i] < rQueue[rLen -1]):
                        rQueue.append(nums[i])
                        rLen += 1
                        i += 1
                    else:
                        lQueue.append(rQueue.pop())
                        lQueue += 1
                        rQueue -= 1
            elif(rLen == 0):        # no ints in right queue
                if(lLen >= k):
                    if(nums[i] > lQueue[lLen-1]):
                        lQueue.append(nums[i])
                        lLen += 1
                        i += 1
                else:
                    if(nums[i] > lQueue[lLen -1]):
                        lQueue.append(nums[i])
                        lLen += 1
                        i += 1
            else:                   # ints in both left and right queues
                if(nums[i] < lQueue[0]):
                    i += 1
        
        
        return 0
    
def main():
    nums = [3,2,1,5,6,4]
    k = 2
    test = Solution()
    print(test.findKthLargest(nums, k))

if(__name__ == "__main__"):
    main()