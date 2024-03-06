# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:
number = 6
def guess(n: int)-> int:
    if(n == number):
        return 0
    elif(n < number):
        return 1

    return -1

class Solution:
    def guessNumber(self, n: int) -> int:
        minNum = 1
        maxNum = n + 1

        curGuess = int((minNum + maxNum)/2)
        result = guess(curGuess)

        while(result != 0):
            if(result < 0):
                maxNum = curGuess
                curGuess = int((minNum + maxNum)/2)
            else:
                minNum = curGuess
                curGuess = int((minNum + maxNum)/2)

            result = guess(curGuess)

        #print(curGuess)
        #print(guess(curGuess))
        return curGuess
    

    
def main():
    test = Solution()
    print(test.guessNumber(10))

if(__name__ == "__main__"):
    main()