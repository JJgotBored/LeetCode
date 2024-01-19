class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l = len(nums)
        max = k
        i = 0
        count = 0

        for j in range(k):
            if(nums[j] == 0):
                count += 1
        
        while((i+max) < l):
            if(nums[i+max] == 0):
                count += 1
            
            if(count <= k):
                max += 1
            else:
                if(nums[i] == 0):
                    count -= 1
                i +=1
        return max
        

def main():
    test = Solution
    print(test.longestOnes(test, [1,1,1,0,0,0,1,1,1,1], 0))

    print(test.longestOnes(test, [1,1,1,0,0,0,1,1,1,1,0], 2))

if(__name__ == "__main__"):
    main()