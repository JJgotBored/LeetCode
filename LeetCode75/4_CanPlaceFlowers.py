class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        possible = 0

        if(len(flowerbed) == 1):
            if(flowerbed[0] == 0 and n <= 1):
                return True
            
        for i in range(len(flowerbed)):
            if(i == 0):
                if(flowerbed[0] == 0 and flowerbed[1] == 0):
                    possible += 1
                    flowerbed[0] = 1
            elif(i == len(flowerbed)-1):
                if(flowerbed[i-1] == 0 and flowerbed[i] == 0):
                    possible += 1
                    flowerbed[i] = 1
            else:
                if(flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0):
                    possible += 1
                    flowerbed[i] = 1

            if(possible >= n):
                return True
        return False

def main():
    #print("Hello World!")
    test = Solution
    print(test.canPlaceFlowers(test, [1,0,0,0,1], 2))

if __name__ == "__main__":
    main()