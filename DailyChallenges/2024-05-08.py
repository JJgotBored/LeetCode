# 506 Relative Ranks 

class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        n = len(score)
        arr = []
        out = [0 for i in range(n)]

        for i in range(n):
            arr.append([score[i], i])

        arr.sort(reverse = True)
        
        for i in range(len(arr)):
            if(i == 0):
                out[arr[i][1]] = "Gold Medal"
            elif(i == 1):
                out[arr[i][1]] = "Silver Medal"
            elif(i == 2):
                out[arr[i][1]] = "Bronze Medal"
            else:
                out[arr[i][1]] = str(i+1)

        return out
    
def main():
    test = Solution()
    scores = [10,3,8,9,4]
    print(test.findRelativeRanks(scores))

if(__name__ == "__main__"):
    main()