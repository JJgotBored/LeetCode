class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if(s[i] == '*'):
                stack.pop()
            else:
                stack.append(s[i])

        return "".join(stack)
        
def main():
    test = Solution
    print(test.removeStars(test, "leet**cod*e"))

if(__name__ == "__main__"):
    main()