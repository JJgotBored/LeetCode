class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        lstS = []
        lstT = []
        lstS[:] = s 
        lstT[:] = t
        count = 0
        lenS = len(lstS)
        lenT = len(lstT)

        if(lenS == 0):
            return True
        elif(lenT == 0):
            return False

        for i in range(lenT):
            if(lstT[i] == lstS[count]):
                count +=1
            if(count >= lenS):
                return True
        return False
    
def main():
    test = Solution
    print(test.isSubsequence(test, "axc", "ahbgdc"))

if(__name__ == "__main__"):
    main()
    