class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        n = len(intervals)
        removed = 0

        print(intervals)
        intervals.sort(key = lambda x: x[1])
        print(intervals)
        interval = intervals[0]
        for i in range(1,n):
            if(intervals[i][0] < interval[1]):
                removed += 1
            else:
                interval[1] = intervals[i][1]

        return removed
    
def main():
    test = Solution()
    #intervals = [[1,2],[2,3],[3,4],[1,3]]
    #intervals = [[1,2],[1,2],[1,2]] 
    #intervals = [[1,2],[2,3]]
    #intervals = [[0,2],[1,3],[2,4],[3,5],[3,5],[4,6],[1,3]]
    intervals = [[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]]

    print(test.eraseOverlapIntervals(intervals))

if(__name__ == "__main__"):
    main()