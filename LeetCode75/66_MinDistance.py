class Solution:
    """
    case 1:
        n1 > n2
        deletes are least costly as switch does not shorten and instert will require an additional delete
    case 2:
        n1 == n2
        switches are least costly as an insert will require a delete and vice versa
    case 3:
        n1 < n2
        inserts are least costly as switch does not increase length and deletes will require aditional insert
    """
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)
        maxActions = max(n1,n2)
        shared = 0
        for i in range(n1):
            print(word1[i])

        return maxActions - shared
    
def main():
    test = Solution()
    word1 = "horse"
    word2 = "ros"

    print(test.minDistance(word1, word2))

if(__name__ == "__main__"):
    main()
