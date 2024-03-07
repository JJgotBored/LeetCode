class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        index = 0
        l = len(nums)
        while(index < l):
            if(index == l-1):
                return index
            elif(nums[index] > nums[index +1]):
                return index
            elif(nums[index] < nums[index +1]):
                index +=1
            else:
                index +=2
        return 0
    
def main():
    #nums = [1,2,3,1]
    nums = [1,2,1,3,5,6,4]
    test = Solution()
    
    print(test.findPeakElement(nums))

if(__name__ == "__main__"):
    main()