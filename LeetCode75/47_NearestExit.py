class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        maze[entrance[0]][entrance[1]] = 'e'
        
        h = len(maze)
        l = len(maze[0])
        paths = [[-1]*l]*h
        exits = []
        max = l*h*10
        paths = [[max]*l for i in range(h)]
        update = []

        #print(maze)
        for i in range(h):
            for j in range(l):
                if(maze[i][j] == '.'):
                    if(i == 0):
                        maze[i][j] = 'E'
                        exits.append([i,j])
                    elif(i == h-1):
                        maze[i][j] = 'E'
                        exits.append([i,j])
                    elif(j == 0):
                        maze[i][j] = 'E'
                        exits.append([i,j])
                    elif(j == l-1):
                        maze[i][j] = 'E'
                        exits.append([i,j])
                elif(maze[i][j] == '+'):
                    paths[i][j] = -1
        
        if(exits == []):
            return -1

        paths[entrance[0]][entrance[1]] = 0
        update.append([entrance[0],entrance[1]])
        temp = []
        while(update != []):            
            temp = update.pop(0)
            if(temp[0]+1 < h):
                if(paths[temp[0]+1][temp[1]] > paths[temp[0]][temp[1]] +1):
                    paths[temp[0]+1][temp[1]] = paths[temp[0]][temp[1]] +1
                    update.append([temp[0]+1,temp[1]])

            if(temp[0]-1 >= 0):
                if(paths[temp[0]-1][temp[1]] > paths[temp[0]][temp[1]] +1):
                    paths[temp[0]-1][temp[1]] = paths[temp[0]][temp[1]] +1
                    update.append([temp[0]-1,temp[1]])

            if(temp[1]+1 < l):
                if(paths[temp[0]][temp[1] +1] > paths[temp[0]][temp[1]] +1):
                    paths[temp[0]][temp[1]+1] = paths[temp[0]][temp[1]] +1
                    update.append([temp[0],temp[1]+1])

            if(temp[1]-1 >= 0):
                if(paths[temp[0]][temp[1] -1] > paths[temp[0]][temp[1]] +1):
                    paths[temp[0]][temp[1]-1] = paths[temp[0]][temp[1]] +1
                    update.append([temp[0],temp[1]-1])

        shortest = max
        for i in exits:
            if(paths[i[0]][i[1]] < shortest):
                shortest = paths[i[0]][i[1]]

        #print(maze)
        #print(paths)
        #print(update)
        #print(exits)
        if(shortest != max):
            return shortest
        
        return -1
    
def main():
    #maze = [["+","+",".","+"],
    #        [".",".",".","+"],
    #        ["+","+","+","."]]
    #entrance = [1,2]
    maze = [["+","+","+"],[".",".","."],["+","+","+"]]
    entrance = [1,0]
    #maze = [[".","+"]]
    #entrance = [0,0]
    test = Solution()
    print(test.nearestExit(maze, entrance))

if(__name__ == "__main__"):
    main()