class Solution:
    def equalPairs(self, grid) -> int:
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = 0
        hash1 = {key: "" for key in range(len(grid))}
        hash2 = {key: "" for key in range(len(grid[0]))}

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                hash1[i] += ","
                hash1[i] += str(grid[i][j])     
                hash2[j] += ","  
                hash2[j] += str(grid[i][j])        

        print(hash1)
        print(hash2)

        for i in hash1.values():
            for j in hash2.values():
                if (i == j):
                    count += 1
        
        return count

def main():
    test = Solution
    print(test.equalPairs(test, [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))

if(__name__ == "__main__"):
    main()