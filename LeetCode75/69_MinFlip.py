class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        aTemp = 0
        bTemp = 0
        cTemp = 0
        count = 0
        while((a + b + c) > 0):
            aTemp = a%2
            bTemp = b%2
            cTemp = c%2
            a = a//2
            b = b//2
            c = c//2

            if(cTemp == 0):
                count = count + aTemp + bTemp
            else:
                count += min(1 - aTemp, 1 - bTemp)
        return count
    
def main():
    test = Solution()
    a = 2
    b = 6
    c = 5

    print(test.minFlips(a,b,c))

if(__name__ == "__main__"):
    main()