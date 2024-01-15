class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        count = 0

        for i in range(l):
            if(nums[i] == 0):
                count += 1
            elif(count > 0):
                nums[i -count] = nums[i]

        for i in range(l-1, l-1-count, -1):
            nums[i] = 0

                
def main():
    #print("hello world")
    test = Solution
    print(test.moveZeroes(test, [0,1,0,3,12,0]))

if(__name__ == "__main__"):
    main()