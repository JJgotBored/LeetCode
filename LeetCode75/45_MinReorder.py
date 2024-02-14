class Solution:
    def __init__(self) -> None:
        self.count = 0

    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        if(n == 0 or n == 1):
            return 0
        graph = [{} for i in range(n)]
        
        visited = {}
        for i in range(n):
            visited[i] = False
        
        for i in range(n-1):
            graph[connections[i][0]][connections[i][1]] = 1
            graph[connections[i][1]][connections[i][0]] = 0
        print(graph)        
        
        self.rSearch(graph, visited, 0)
        return self.count
    
    def rSearch(self, graph: list[dict], visited: list[int], city: int):
        if(visited[city] == False):
            visited[city] = True
            for road in graph[city].keys():
                if(visited[road] == False):
                    self.count += graph[city][road]
                    self.rSearch(graph, visited, road)
        return

def main():
    #n = 6
    #connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
    n = 5
    connections = [[1,0],[1,2],[3,2],[3,4]]
    #n = 3
    #connections = [[1,0],[1,2]]
    test = Solution()

    print(test.minReorder(n, connections))

if(__name__ == "__main__"):
    main()