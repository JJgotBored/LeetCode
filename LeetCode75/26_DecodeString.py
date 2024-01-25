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
                depth -= 1
                temp2 = s[i]

                if(temp1.isdigit() and temp2.isdigit()):
                    temp1 += temp2
                    stack.append(temp1)
                    depth += 1
                elif(temp1.isalpha() and temp2.isalpha()):
                    temp1 += temp2
                    stack.append(temp1)
                    depth += 1
                elif(temp2 == "["):
                    stack.append(temp1)
                    depth += 1
                elif(temp2 == "]"):
                    temp2 = stack.pop()
                    if(temp2.isdigit()):
                        temp1 *= int(temp2)
                    elif(temp2.isalpha):
                        temp1 = temp2 + temp1
                    stack.append(temp1)
                else:
                    stack.append(temp1)
                    stack.append(temp2)
                    depth += 2
                

                #print(temp1, temp2)
            print((stack))

        return ""
        
def main():
    test = Solution
    print(test.decodeString(test, "3[a2[c]]"))

if(__name__ == "__main__"):
    main()