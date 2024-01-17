class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = {"a","e","i","o","u"}
        l = len(s)
        sList =[]
        sList[:] = s
        count = 0
        max = 0

        for i in range(k):
            if(sList[i] in vowels):
                count += 1
        max = count

        for i in range(k,l,1):
            if(sList[i-k] in vowels):
                count -= 1
            if(sList[i] in vowels):
                count += 1
            if(count > max):
                max = count
        return max

def main():
    test = Solution
    print(test.maxVowels(test,"leetcode", 3))

if(__name__ == "__main__"):
    main()