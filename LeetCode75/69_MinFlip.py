class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        return abs(a + b -c)
    
def main():
    test = Solution()
    a = 2
    b = 6
    c = 5

    print(test.minFlips(a,b,c))

if(__name__ == "__main__"):
    main()