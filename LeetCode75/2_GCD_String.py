class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if(str1 == str2):
            return str1

        substring = ""

        if(len(str1)>=len(str2)):
            for i in range(len(str2)):
                temp = str2[0:i+1]
                
                multi1 = int(len(str1)/(i+1))
                multi2 = int(len(str2)/(i+1))

                if(temp * multi1 == str1 and temp * multi2 == str2):
                    substring = temp[:]
                
        else:
            for i in range(len(str1)):
                temp = str1[0:i+1]
                multi1 = int(len(str1)/(i+1))
                multi2 = int(len(str2)/(i+1))

                if(temp * multi1 == str1 and temp * multi2 == str2):
                    substring = temp[:]

        return substring
    
def main():
    print("Hello World!")
    test = Solution
    print(test.gcdOfStrings(test, "ABABAB", "ABAB"))

if __name__ == "__main__":
    main()