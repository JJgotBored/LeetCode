class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        dict1 = {key:1 for key in nums1 }
        dict2 = {key:1 for key in nums2 }
        lst1 = []
        lst2 = []

        for i in dict1.keys():
            if( i not in dict2):
                lst1.append(i)

        for i in dict2.keys():
            if( i not in dict1):
                lst2.append(i)

        return [lst1, lst2]

def main():
    test = Solution
    print(test.findDifference(test, [1,2,3], [2,4,6]))

if(__name__ == "__main__"):
    main()