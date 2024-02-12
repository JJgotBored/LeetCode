class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        if(n == 0 or n == 1):
            return 0
        hash = {}
        hash[0] = True

        for i in range(n-1):
            if(connections[i][1] == 0):
                hash[connections[i][0]] = True
            elif(hash.get(connections[i][0]) == None):
                hash[connections[i][0]] = False

        print(hash)        

        return 0
    
    def rSearch(self, n: int, depth: int, connections: list[list[int]])-> int:

        return 0

def main():
    n = 6
    connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
    test = Solution()

    print(test.minReorder(n, connections))

if(__name__ == "__main__"):
    main()