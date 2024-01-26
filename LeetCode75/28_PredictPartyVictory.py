class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        queue = []
        numR = 0
        numD = 0
        bansR = 0
        bansD = 0
        temp = ""

        for i in range(len(senate)):
            if(senate[i] =="R"):
                numR += 1
            else:
                numD += 1
            queue.append(senate[i])

        #print(queue)
        #print(numR, numD)
        
        while(numD > 0 and numR > 0):
            temp = queue.pop(0)

            if(temp == "R"):
                if(bansR == 0):
                    bansD += 1
                    queue.append(temp)
                else:
                    numR -= 1
                    bansR -= 1
            else:
                if(bansD == 0):
                    bansR += 1
                    queue.append(temp)
                else:
                    numD -= 1
                    bansD -= 1

        if(numR > 0):
            return "Radiant"
        return "Dire"

def main():
    test = Solution
    print(test.predictPartyVictory(test, "RDDR"))

if(__name__ == "__main__"):
    main()