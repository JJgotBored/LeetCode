class Solution:
    """
    case 1:
        n1 > n2
        deletes are least costly as switch does not shorten and instert will require an additional delete
        delete costs 1 action
        switch costs 2 actions
        insert costs 3 actions
    case 2:
        n1 == n2
        switches are least costly as an insert will require a delete and vice versa
        insert and delete are only worth while if they shift what would other wise require 3 or more switches
        switch costs 1 action
        delete costs 2 actions
        insert costs 2 actions  
    case 3:
        n1 < n2
        inserts are least costly as switch does not increase length and deletes will require aditional insert
        insert costs 1 action
        switch costs 2 actions
        delete costs 3 actions
    """
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)
        maxActions = max(n1,n2)
        
        if(word1 == "" or word2 == ""):
            return maxActions
        
        arr1 = [500 for i in range(maxActions+1)]
        arr2 = [i for i in range(maxActions+1)]

        if(word1[0] == word2[0]):
            arr1[0] = 0
        else:
            arr1[0] = 1

        
        for i in range(1,n1+1):
            for j in range(1, n2+1):
                if(word1[i-1] == word2[j-1]):
                    arr1[j] = arr2[j-1]
                else:
                    arr1[j] = min(arr1[j-1], arr2[j-1], arr2[j]) +1
            print(arr2)
            arr2 = arr1[:]

        #print(arr2)
        #print(arr1)

        return arr2[n2]
    
def main():
    test = Solution()
    #word1 = "horse"
    #word1 = "intention"
    word1 = "dinitrophenylhydrazine"

    #word2 = "ros"
    word2 = "execution"
    word2 = "dimethylhydrazine"

    print(test.minDistance(word1, word2))

if(__name__ == "__main__"):
    main()
