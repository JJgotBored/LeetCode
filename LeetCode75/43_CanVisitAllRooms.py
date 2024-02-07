class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        visited = {}
        for i in range(len(rooms)):
            visited[i] = False
        
        self.searchRooms(rooms, visited, 0)

        if(False in visited.values()):
            return False
        return True
    
    def searchRooms(self, rooms: list[list[int]], visited: dict, currRoom: int):
        if(visited[currRoom] == True):
            return
        visited[currRoom] = True
        for i in range(len(rooms[currRoom])):
            self.searchRooms(rooms, visited, rooms[currRoom][i])
        return
    

def main():
    #rooms = [[1],[2],[3],[]]
    rooms = [[1,3],[3,0,1],[2],[0]]
    test = Solution()
    print(test.canVisitAllRooms(rooms))

if(__name__ == "__main__"):
    main()