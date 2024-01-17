class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        sum = 0
        maxSum = 0
        l = len(nums)
        for i in range(k):
            sum += nums[i]
        
        maxSum = sum

        for i in range(k, l, 1):
            sum = sum - nums[i-k] + nums[i]
            if(sum > maxSum):
                maxSum = sum
        return float(maxSum)/k


def main():
    test = Solution
    print(test.findMaxAverage(test,[0,4,0,3,2], 1))

if(__name__ == "__main__"):
    main()