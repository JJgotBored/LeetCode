class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        n = len(piles)
        piles.sort()
        left = 1
        right = piles[n-1]
        mid = 0

        if(h == n):
            return piles[n-1]
        
        while(left < right):
            mid = (left + right)//2
            if(self.checkEaten(piles, h, mid)):
                right = mid
            else:
                left = mid +1
        return left
    
    def checkEaten(self, piles: list[int], h: int, speed: int) -> bool:
        count = 0
        for i in piles:
            count += i//speed
            if(i%speed > 0):
                count += 1

        return count <= h
    
def main():
    #piles = [3,6,7,11]
    #h = 8

    piles = [30,11,23,4,20]
    #h = 5
    h = 6

    test = Solution()

    print(test.minEatingSpeed(piles, h))

if(__name__ == "__main__"):
    main()
        