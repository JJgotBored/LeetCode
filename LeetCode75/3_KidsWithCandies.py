class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        largest = 0
        output = [False for i in range(len(candies))]

        for i in range(len(candies)):
            if(candies[i] > largest):
                largest = candies[i]
        
        for i in range(len(candies)):
            if(candies[i] + extraCandies >= largest):
                output[i] = True


        return output

def main():
    print("Hello World!")
    test = Solution
    print(test.kidsWithCandies(test, [12,1,12], 10))

if __name__ == "__main__":
    main()