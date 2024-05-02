class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        n = len(intervals)
        matrix = [[ 0 for i in range(n)] for j in range(n)]
        sums = [0 for i in range(n)]
        clashes = 0
        removed = 0
        index = 0

        for i in range(n):
            for j in range(n):
                if(i != j):
                    if(intervals[i][0] <= intervals[j][0] and intervals[i][1] > intervals[j][0]):
                        matrix[i][j] = 1
                        clashes += 1
                        sums[i] += 1
                    
                    elif(intervals[i][0] < intervals[j][1] and intervals[i][1] >= intervals[j][1]):
                        matrix[i][j] = 1
                        clashes += 1
                        sums[i] += 1

        for i in matrix:
            print(i)

        print(clashes)
        print(sums)

        while(clashes > 0):
            index = sums.index(max(sums))

            for i in range(n):
                if(matrix[index][i] == 1):
                    matrix[index][i] = 0
                    matrix[i][index] = 0
                    clashes -= 2
                    sums[index] -= 1
                    sums[i] -= 1
                    
            removed += 1
            print(clashes)
            print(sums)
        return removed
    
def main():
    test = Solution()
    #intervals = [[1,2],[2,3],[3,4],[1,3]]
    #intervals = [[1,2],[1,2],[1,2]] 
    #intervals = [[1,2],[2,3]]
    intervals = [[0,2],[1,3],[1,3],[2,4],[3,5],[3,5],[4,6]]

    print(test.eraseOverlapIntervals(intervals))

if(__name__ == "__main__"):
    main()