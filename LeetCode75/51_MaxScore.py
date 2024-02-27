class Solution:
    def maxScore(self, nums1: list[int], nums2: list[int], k: int) -> int:
        l = len(nums1)
        subset = []
        curSum = 0
        newSum = 0
        curSmallest = 10000
        index = 0

        for i in range(l):
            subset.append([nums1[i], nums2[i]])
            curSum += nums1[i]
            
            if(len(subset) > k):
                index = 0
                newSum = curSum - subset[0][0]


        print(subset)
        return 0

def main():
    nums1 = [1,3,3,2]
    nums2 = [2,1,3,4]
    k = 3
    test = Solution()
    print(test.maxScore(nums1, nums2, k))

if(__name__ == "__main__"):
    main()