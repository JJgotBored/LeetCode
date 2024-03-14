class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        out = []
        #used = {}
        #for i in range(1,10):
        #    used[i] = 0

        self.recSum(k, 0, n, 0, [], 1, out)
        return out
    
    def recSum(self, maxDepth: int, curDepth: int, maxSum: int, curSum: int, combo: list[int], start: int, out: list[list[int]]):
        if(curDepth == maxDepth ):
            if(curSum == maxSum):
                out.append(combo[:])
                #print(combo)
            return
        elif(curSum >= maxSum):
            return

        for i in range(start,10):
            combo.append(i)
            curSum += i
            self.recSum(maxDepth, curDepth +1, maxSum, curSum, combo, i +1, out)
            combo.pop()
            curSum -= i

        return
    
def main():
    k = 4
    n = 1
    test = Solution()
    print(test.combinationSum3(k, n))

if(__name__ == "__main__"):
    main()
        