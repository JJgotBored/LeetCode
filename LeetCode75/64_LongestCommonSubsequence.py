class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if(text1 == text2):
            return len(text1)
        l1 = len(text1)
        l2 = len(text2)
        s1 = list(text1.strip())
        s2 = list(text2.strip())

        previous = [0 for i in range(l2+1)]
        current = [0 for i in range(l2+1)]

        for i in range(1, l1+1):
            for j in range(1, l2+1):
                if(s1[i-1] == s2[j-1]):
                    current[j] = 1 + previous[j-1]
                else:
                    current[j] = max(previous[j], current[j-1])
            previous = current[:]

        #print(previous)
        #print(current)
        #print(s1)
        #print(s2)

        return previous[l2]
    
def main():
    s1 = "ab"
    s2 = "abc"
    test = Solution()
    print(test.longestCommonSubsequence(s1,s2))

if(__name__ == "__main__"):
    main()