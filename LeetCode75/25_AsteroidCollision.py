class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        sl = 0
        al = len(asteroids)
        temp1 = 0
        temp2 = 0
        i = 0

        while(i < al):
            if(sl == 0):
                stack.append(asteroids[i])
                sl += 1
                i += 1
            else:
                temp1 = stack.pop()
                sl -= 1
                temp2 = asteroids[i]

                if((not(temp1 > 0)) or (not(temp2 < 0))):
                    stack.append(temp1)
                    stack.append(temp2)
                    sl += 2
                    i += 1
                elif(abs(temp1) > abs(temp2)):
                    stack.append(temp1)
                    sl += 1
                    i += 1
                elif(abs(temp1) == abs(temp2)):
                    i += 1
        
        return stack
    
def main():
    test = Solution
    print(test.asteroidCollision(test, [10, 9,7, -8]))

if(__name__ == "__main__"):
    main()