class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        l = len(nums)
        left = 0
        right = l-1
        mid = 0

        while(left <= right):
            mid = (left + right)//2
            if(mid < l-1 and nums[mid] < nums[mid +1]):
                left = mid +1
            elif(mid > 0 and nums[mid] < nums[mid -1]):
                right = mid -1
            else:
                return mid
        return 0
    
def main():
    nums = [1,2,3,1]
    #nums = [1,2,1,3,5,6,4]
    test = Solution()
    
    print(test.findPeakElement(nums))

if(__name__ == "__main__"):
    main()