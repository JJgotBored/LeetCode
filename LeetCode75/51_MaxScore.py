class Solution:

    def maxScore(self, nums1: list[int], nums2: list[int], k: int) -> int:
        l = len(nums1)
        pairs = []
        subset = []
        curSum = 0
        tempMax = 0
        index = 0

        for i in range(l):
            pairs.append([nums2[i], nums1[i]])  
        pairs.sort(reverse = True)
        print(pairs)
        
        for i in pairs:
            subset.append(i)
            curSum += i[1]

            if(len(subset) > k):
                index = k
                tempMax = (curSum - subset[k][1])* subset[k-1][0]
                print(subset)
                
                for j in range(0, k):
                    print(j)
                    if(tempMax < (curSum - subset[j][1])*subset[k][0]):
                        tempMax = (curSum - subset[j][1])*subset[k][0]
                        index = j
                curSum -= subset[index][1]
                subset.pop(index)
        
        print(subset)
        return curSum * subset[k-1][0]

def main():
    #nums1 = [1,3,3,2]
    #nums2 = [2,1,3,4]
    #k = 3
    #nums1 = [4,2,3,1,1]
    #nums2 = [7,5,10,9,6]
    #k = 1
    nums1 = [22,5,25,15,28,1]
    nums2 = [22,30,25,25,9,18]
    k = 3
    test = Solution()
    print(test.maxScore(nums1, nums2, k))

if(__name__ == "__main__"):
    main()