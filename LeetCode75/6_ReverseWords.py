class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        arr = s.split()
        arr = arr[::-1]
        output = " ".join(arr)

        return output


def main():
    #print("Hello World!")
    test = Solution
    print(test.reverseWords(test, " the sky is blue"))

if __name__ == "__main__":
    main()