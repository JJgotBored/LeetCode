class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        
        update = []
        next = []
        fresh = 0
        minutes = 0
        h = len(grid)
        l = len(grid[0])

        for i in range(h):
            for j in range(l):
                if(grid[i][j] == 1):
                    fresh += 1
                elif(grid[i][j] == 2):
                    update.append([i,j])
        if(fresh == 0):
            return 0
    
        while(update != []):
            #self.printGrid(grid)
            for i in update:
                if(i[0]+1 < h):
                    if(grid[i[0]+1][i[1]] == 1):
                        grid[i[0]+1][i[1]] = 2
                        fresh -= 1
                        next.append([i[0]+1, i[1]])
                if(i[0]-1 >= 0):
                    if(grid[i[0]-1][i[1]] == 1):
                        grid[i[0]-1][i[1]] = 2
                        fresh -= 1
                        next.append([i[0]-1, i[1]])
                if(i[1]+1 < l):
                    if(grid[i[0]][i[1]+1] == 1):
                        grid[i[0]][i[1]+1] = 2
                        fresh -= 1
                        next.append([i[0], i[1]+1])
                if(i[1]-1 >= 0):
                    if(grid[i[0]][i[1]-1] == 1):
                        grid[i[0]][i[1]-1] = 2
                        fresh -= 1
                        next.append([i[0], i[1]-1])

            update = next[:]
            next = [][:]
            minutes += 1
            #print("minutes: ", minutes)

        if(fresh == 0):
            return minutes -1
        #print(fresh)
        #print(update)
        return -1
    
    def printGrid(self, grid: list[list[int]]):
        for i in grid:
            print(i)
        print("")
    

def main():
    #grid = [[2,1,1],[1,1,0],[0,1,1]]
    #grid = [[2,1,1],[0,1,1],[1,0,1]]
    grid = [[0,2]]
    test = Solution()
    print(test.orangesRotting(grid))

if(__name__ == "__main__"):
    main()