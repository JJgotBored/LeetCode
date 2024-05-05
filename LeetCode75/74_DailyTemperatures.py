class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        # try implementing a monotonic stack populated by parsing the list in reverse 
        n = len(temperatures)
        out = [0 for i in range(n)]
        return out

def main():
    test = Solution()
    temperatures = [73,74,75,71,69,72,76,73]
    print(test.dailyTemperatures(temperatures))

if(__name__ == "__main__"):
    main()