# 506 Relative Ranks 

class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        arr = []
        out = [0 for i in len(score)]
        for i in range(len(score)):
            arr.append([score[i], i])

        arr.sort()
        
        for i in range(len(arr)):
            if(i == 0):
                out[arr[1]] = "First"


        return None
    
def main():
    test = Solution()
    scores = []
    print(test.findRelativeRanks(scores))

if(__name__ == "__main__"):
    main()