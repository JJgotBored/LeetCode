class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        hash1 = {}
        hash2 = {}

        for i in word1:
            if(i in hash1):
                hash1[i] += 1
            else:
                hash1[i] = 1
        
        for i in word2:
            if(i in hash2):
                hash2[i] += 1
            else:
                hash2[i] = 1

        lst1 = sorted(list(hash1.values()))
        lst2 = sorted(list(hash2.values()))

        keys1 = sorted(list(hash1.keys()))
        keys2 = sorted(list(hash2.keys()))

        if(lst1 == lst2 and keys1 == keys2):
            return True
        return False

def main():
    test = Solution
    print(test.closeStrings(test, "cabbba", "abbccc"))

if(__name__ == "__main__"):
    main()