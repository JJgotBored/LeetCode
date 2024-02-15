class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:

        graph = {}
        for i in equations:
            for j in i:
                if((j in graph.keys()) == False):
                    graph[j] = {}
                    graph[j][j] = 1

        l = len(values)
        for i in range(l):
            graph[equations[i][0]][equations[i][1]] = values[i]
            graph[equations[i][1]][equations[i][0]] = 1/values[i]

        #print(graph)

        out = []
        for i in range(len(queries)):
            out.append(self.rSearch(graph, queries[i][0], queries[i][1], 1.0, {}))

        return out
    
    def rSearch(self, graph: dict[dict], curVar: str, searchVar: str, curVal: float, visited: dict) -> float:
        #if search or current are not in graph
        if((curVar not in graph.keys()) or (searchVar not in graph.keys())):
            
            return -1.0
        #if node has already been visited
        if(curVar in visited.keys()):
            return -1.0
        
        visited[curVar] = True
        temp = -1.0
        if(curVar == searchVar):
            return curVal
        elif(searchVar in graph[curVar].keys()):
            return curVal*graph[curVar][searchVar]
        else:
            for i in graph[curVar].keys():
                temp = self.rSearch(graph, i, searchVar, curVal * graph[curVar][i], visited)
                if(temp != -1.0):
                    return temp
        return -1.0

def main():
    #equ = [["a","b"],["b","c"]]
    #vals = [2.0,3.0]
    #ques = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]

    #equ = [["a","b"],["b","c"],["bc","cd"]]
    #vals = [1.5,2.5,5.0]
    #ques = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]

    equ = [["a","b"]]
    vals = [0.5]
    ques = [["a","b"],["b","a"],["a","c"],["x","y"]]

    test = Solution()
    print(test.calcEquation(equ, vals, ques))

if(__name__ == "__main__"):
    main()