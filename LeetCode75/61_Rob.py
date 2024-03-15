class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        loot = [0]*n

        for i in range(n):
            if(i < 2):
                loot[i] = nums[i]
            elif(i == 2):
                loot[i] = nums[i] + nums[i-2]
            else:
                loot[i] = max(loot[i-2], loot[i-3])+ nums[i]

        #print(nums)
        #print(loot)
        return max(loot[n-1], loot[n-2])
    
def main():
    #nums = [1,2,3,1]
    nums = [2,7,9,3,1]
    test = Solution()
    print(test.rob(nums))

if(__name__ == "__main__"):
    main()