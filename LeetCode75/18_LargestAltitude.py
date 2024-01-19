class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        alt = 0
        max = 0

        for i in range(len(gain)):
            alt += gain[i]
            if(alt > max):
                max = alt
        return max

def main():
    test = Solution
    print(test.largestAltitude(test, [-5,1,5,0,-7]))

if(__name__ == "__main__"):
    main()