class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height)-1

        max = min(height[left],height[right])*(right-left)
        while(left < right):
            if(height[left] < height[right]):
                left += 1
            else:
                right -=1
            if(max < min(height[left],height[right])*(right-left)):
                max = min(height[left],height[right])*(right-left)
        return max
        
def main():
    test = Solution
    print(test.maxArea(test, [2,3,4,5,18,17,6]))

if(__name__ == "__main__"):
    main()