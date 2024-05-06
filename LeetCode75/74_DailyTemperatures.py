class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        # try implementing a monotonic stack populated by parsing the list in reverse 
        n = len(temperatures)
        out = [0 for i in range(n)]
        stack = []

        for i in range(n-1, -1, -1):
            print(i)

            while( len(stack) > 0 and stack[len(stack)-1][0] <= temperatures[i]):
                    stack.pop()


            if(len(stack) == 0):
                stack.append([temperatures[i], i])
                out[i] = 0
            else:
                out[i] = stack[len(stack)-1][1] -i
                stack.append([temperatures[i], i])
                

        return out

def main():
    test = Solution()
    temperatures = [73,74,75,71,69,72,76,73]
    print(test.dailyTemperatures(temperatures))

if(__name__ == "__main__"):
    main()