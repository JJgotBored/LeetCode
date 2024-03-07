class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        l = len(potions)
        ans = []
        left = 0
        right = l-1
        temp = 0

        potions.sort()

        for i in spells:
            left = 0
            right = l-1

            if(i * potions[left] >= success):
                ans.append(l)
            elif(i * potions[right] < success):
                ans.append(0)
            else:
                temp = int((left + right)/2)
                while( left != temp):
                    if(i * potions[temp] >=  success):
                        right = temp
                        temp = int((left + right)/2)
                    else:
                        left = temp
                        temp = int((left + right)/2)
                ans.append(l-right)

        #print(potions)

        return ans
    
def main():
    #spells = [5,1,3]
    #potions = [1,2,3,4,5]
    #success = 7

    spells = [3,1,2]
    potions = [8,5,8]
    success = 16

    test = Solution()
    print(test.successfulPairs(spells, potions, success))

if(__name__ == "__main__"):
    main()
        