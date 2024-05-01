class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        n = len(intervals)
        matrix = [[ 0 for i in range(n)] for j in range(n)]
        count = 0

        for i in range(n):
            for j in range(n):
                if(i != j):
                    if(intervals[i][0] <= intervals[j][0] and intervals[i][1] > intervals[j][0]):
                        matrix[i][j] = 1
                        count += 1
                    
                    elif(intervals[i][0] < intervals[j][1] and intervals[i][1] >= intervals[j][1]):
                        matrix[i][j] = 1
                        count += 1

        for i in matrix:
            print(i)

        print(count)
        return 0
    
def main():
    test = Solution()
    intervals = [[1,2],[2,3],[3,4],[1,3]] 
    print(test.eraseOverlapIntervals(intervals))

if(__name__ == "__main__"):
    main()