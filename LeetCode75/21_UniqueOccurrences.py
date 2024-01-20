class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        hash1 = {key: 0 for key in arr }

        for i in range(len(arr)):
            hash1[arr[i]] += 1

        hash2 = {key: 1 for key in hash1.values()}

        if(len(hash1) == len(hash2)):
            return True
        return False

def main():
    test = Solution
    print(test.uniqueOccurrences(test, [1,2]))

if(__name__ == "__main__"):
    main()