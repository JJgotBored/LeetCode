class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key = lambda x:x[1])
        #print(points)
        arrows = 0
        lastArrow = points[0][0] -1

        for i in points:
            if(i[0] > lastArrow):
                arrows += 1
                lastArrow = i[1]

        return arrows
    
def main():
    test = Solution()
    #points = [[10,16],[2,8],[1,6],[7,12]]
    #points = [[1,2],[3,4],[5,6],[7,8]]
    points = [[1,2],[2,3],[3,4],[4,5]]
    print(test.findMinArrowShots(points))

if(__name__ == "__main__"):
    main()