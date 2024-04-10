class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        singles = {}
        #n = len(nums)
        for i in nums:
            if(i in singles.keys()):
                singles.pop(i)
            else:
                singles[i] = 1
                
        return list(singles.keys())[0]
    
def main():
    test = Solution()
    #nums = [2,2,1]
    nums = [4,1,2,1,2]

    print(test.singleNumber(nums))

if(__name__ == "__main__"):
    main()