class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        if(isConnected == []):
            return 0
        
        n = len(isConnected)
        visited = {}
        provinces = 0

        for i in range(n):
            visited[i] = False

        for i in range(n):
            if(visited[i] == False):
                self.rSearch(isConnected, i,visited, n)
                provinces += 1

        return provinces
    
    def rSearch(self, isConnected: list[list[int]], curr: int, visited: dict, n: int):
        if(visited[curr] == True):
            return
        visited[curr] = True
        for i in range(n):
            if(isConnected[curr][i] == 1):
                self.rSearch(isConnected, i, visited, n)
        return 
    
def main():
    input = [[1,1,0],[1,1,0],[0,0,1]]
    test = Solution()
    print(test.findCircleNum(input))

if(__name__ == "__main__"):
    main()
        