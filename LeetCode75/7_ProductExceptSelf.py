class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = len(nums)

        output = [1 for i in range(l)]
        pre = 1
        post = 1

        for i in range(l):
            output[i] *= pre
            pre *= nums[i]
        for i in range(l-1,-1,-1):
            output[i] *= post
            post *= nums[i]

        return output
        
def main():
    #print("Hello World!")
    test = Solution
    print(test.productExceptSelf(test, [1,2,3,4]))

if __name__ == "__main__":
    main()