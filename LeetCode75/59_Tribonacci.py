class Solution:
    def tribonacci(self, n: int) -> int:
        if(n == 0):
            return 0
        num1 = 0
        num2 = 0
        num3 = 1
        curSum = 1
        counter = 1

        while(counter < n):
            curSum = num1 + num2 + num3
            num1 = num2
            num2 = num3
            num3 = curSum
            counter += 1
        return curSum
    
def main():
    n = 4
    test = Solution()
    print(test.tribonacci(n))

if(__name__ == "__main__"):
    main()