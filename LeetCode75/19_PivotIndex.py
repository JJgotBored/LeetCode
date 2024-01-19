class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        sum1 = 0
        sum2 = 0

        for i in range(l):
            sum1 += nums[i]
        
        for i in range(l):
            if(sum2 == float(sum1 - nums[i])/2):
                return i
            else:
                sum2 += nums[i]
        return -1

def main():
    test = Solution
    print(test.pivotIndex(test,[-1,-1,-1,-1,-1,-1]))

if(__name__ == "__main__"):
    main()