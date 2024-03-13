class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        out = []
        used = {}
        for i in range(1,10):
            used[i] = 0

        self.recSum(k, 0, n, 0, [], used, out)
        return out
    
    def recSum(self, maxDepth: int, curDepth: int, maxSum: int, curSum: int, combo: list[int], used: dict, out: list[list[int]]):
        if(curDepth == maxDepth ):
            if(curSum == maxSum):
                out.append(combo[:])
                print(combo)
            return
        elif(curSum >= maxSum):
            return

        for i in range(curDepth + 1,10):
            if(used[i] == 0):
                combo.append(i)
                curSum += i
                used[i] = 1
                self.recSum(maxDepth, curDepth +1, maxSum, curSum, combo, used, out)
                combo.pop()
                curSum -= i
                used[i] = 0

        return
    
def main():
    k = 3
    n = 9
    test = Solution()
    print(test.combinationSum3(k, n))

if(__name__ == "__main__"):
    main()
        