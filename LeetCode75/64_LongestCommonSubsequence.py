class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if(text1 == text2):
            return len(text1)
        l1 = len(text1)
        l2 = len(text2)

        
        return 0
    
def main():
    s1 = "ab"
    s2 = "abc"
    test = Solution()
    print(test.longestCommonSubsequence(s1,s2))

if(__name__ == "__main__"):
    main()