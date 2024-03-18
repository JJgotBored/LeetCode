class Solution:
    def numTilings(self, n: int) -> int:
        i = 1
        a = 1
        b = 1
        c = 0
        d = 0
        while(i < n):
            d = c
            c = b
            b = a
            a = 2 * b + d
            #print(a, b, c, d)
            i += 1
        return a
    
def main():
    num = 6
    test = Solution()
    print(test.numTilings(num))

if(__name__ == "__main__"):
    main()