class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        l = len(nums)
        check = [0 for i in range(l)]
        min = nums[0]
        max = nums[l-1]
        
        #check if nums[i] is larger than a previous index
        for i in range(l):
            if(nums[i] <= min):
                min = nums[i]
            else:
                check[i] += 1

        #check if nums[i] is smaller than a following index
        for i in range(l-1,-1,-1):
            if(nums[i] >= max):
                max = nums[i]
            else:
                check[i] += 1
        #check if an index exists such that it has been incremented twice
        for i in range(l):
            if(check[i] == 2):
                return True

        return False

def main():
    test = Solution
    print(test.increasingTriplet(test, [2,1,5,0,4,6]))

if(__name__ == "__main__"):
    main()