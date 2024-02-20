class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        maze[entrance[0]][entrance[1]] = 'e'
        
        h = len(maze)
        l = len(maze[0])
        exits = []
        print(maze)
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

        print(maze)
        print(exits)
        return 0
    
def main():
    maze = [["+","+",".","+"],
            [".",".",".","+"],
            ["+","+","+","."]]
    entrance = [1,2]
    test = Solution()
    print(test.nearestExit(maze, entrance))

if(__name__ == "__main__"):
    main()