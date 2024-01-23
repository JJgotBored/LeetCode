class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        depth = 0
        l = len(s)
        temp1 = ""
        temp2 = ""


        for i in range(l):
            if(depth == 0):
                stack.append(s[i])
                depth += 1
            else:
                temp1 = stack.pop()
                temp2 = s[i]
                print(temp1, temp2)
            print(stack)

        return ""
        
def main():
    test = Solution
    print(test.decodeString(test, "3[a]2[bc]"))

if(__name__ == "__main__"):
    main()