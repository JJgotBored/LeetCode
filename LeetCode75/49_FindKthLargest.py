class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        lQueue = []
        rQueue = []
        lLen = 0
        rLen = 0
        l = len(nums)
        i = 0

        while(i < l):
            #print(lQueue, rQueue)
            if(lLen + rLen < k):
                if(lLen == 0 and rLen == 0):
                   lQueue.append(nums[i])
                   lLen += 1
                   i += 1
                elif(lLen == 0):
                    if(nums[i] <= rQueue[rLen -1]):
                        rQueue.append(nums[i])
                        rLen += 1
                        i += 1
                    else:
                        lQueue.append(rQueue.pop())
                        lLen +=1
                        rLen -= 1
                elif(rLen == 0):
                    if(nums[i] >= lQueue[lLen -1]):
                        lQueue.append(nums[i])
                        lLen += 1
                        i += 1
                    else:
                        rQueue.append(lQueue.pop())
                        rLen += 1
                        lLen -= 1
                else:
                    if((lQueue[lLen -1]) <= nums[i] and nums[i] <= rQueue[rLen -1]):
                        lQueue.append(nums[i])
                        lLen += 1
                        i +=1
                    elif(lQueue[lLen -1] > nums[i]):
                        rQueue.append(lQueue.pop())
                        rLen += 1
                        lLen -= 1
                    elif(rQueue[rLen -1] < nums[i]):
                        lQueue.append(rQueue.pop())
                        lLen += 1
                        rLen -= 1
            else:
                if(lLen == 0):
                    if(nums[i] <= rQueue[rLen -1]):
                        i += 1
                    elif(rQueue[0] <= nums[i]):
                        rQueue.pop()
                        rQueue.insert(0, nums[i])
                        i +=1
                    else:
                        lQueue.append(rQueue.pop())
                        lLen += 1
                        rLen -= 1
                elif(rLen == 0):
                    if(nums[i] <= lQueue[0]):
                        i += 1
                    elif(lQueue[lLen -1] <= nums[i]):
                        lQueue.pop(0)
                        lQueue.append(nums[i])
                        i += 1
                    else:
                        rQueue.append(lQueue.pop())
                        rLen += 1
                        lLen -= 1
                else:
                    if(nums[i] <= lQueue[0]):
                        i += 1
                    elif(rQueue[0] <= nums[i]):
                        rQueue.insert(0, nums[i])
                        rLen += 1
                        lQueue.pop(0)
                        lLen -= 1
                        i += 1
                    elif(lQueue[lLen -1] <= nums[i] and nums[i] <= rQueue[rLen -1]):
                        lQueue.pop(0)
                        lQueue.append(nums[i])
                        i += 1
                    elif(nums[i] < lQueue[lLen -1]):
                        rQueue.append(lQueue.pop())
                        rLen += 1
                        lLen -= 1
                    elif(rQueue[rLen -1] < nums[i]):
                        lQueue.append(rQueue.pop())
                        lLen += 1
                        rLen -= 1

        while(rQueue != []):
            lQueue.append(rQueue.pop())
        #print(lQueue)
        #print(rQueue)    
        
        return lQueue[0]
    
def main():
    #nums = [3,2,1,5,6,4]
    #k = 2
    nums = [3,2,3,1,2,4,5,5,6]
    k = 4
    test = Solution()
    print(test.findKthLargest(nums, k))

if(__name__ == "__main__"):
    main()