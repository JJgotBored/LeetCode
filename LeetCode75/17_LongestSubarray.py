class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        max = 0
        count = 0
        i = 0

        while((i+max) < l):
            if(nums[i+max] == 0):
                count += 1

            if(count <= 1):
                max += 1
            else:
                if(nums[i] == 0):
                    count -= 1
                i += 1
        
        max -= 1
        return max   
         
def main():
    test = Solution
    print(test.longestSubarray(test, [1,1,0,1]))

if(__name__ == "__main__"):
    main()