class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        arr = [[0 for i in range(n)]for j in range(m)]
        #arr[0][0] = 1

        for i in range(m):
            for j in range(n):
                if(i == 0 and j == 0):
                    arr[i][j] = 1
                elif(i == 0):
                    arr[i][j] = arr[i][j-1]
                elif(j == 0):
                    arr[i][j] = arr[i-1][j]
                else:
                    arr[i][j] = arr[i][j-1] + arr[i-1][j]

        #print(arr)
        return arr[m-1][n-1]
    
def main():
    m = 3
    n = 7
    test = Solution()
    print(test.uniquePaths(m,n))

if(__name__ == "__main__"):
    main()