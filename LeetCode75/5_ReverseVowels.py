class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        index = 0
        vowels = ""
        output = ""
        for i in range(len(s)):
            if(s[i] == 'a' or s[i] == 'A' or s[i] == 'e' or s[i] == 'E' or s[i] == 'i' or s[i] == 'I' or s[i] == 'o' or s[i] == 'O'or s[i] == 'u' or s[i] == 'U'):
                vowels += s[i]

        vowels = vowels[::-1]
        for i in range(len(s)):
            if(s[i] == 'a' or s[i] == 'A' or s[i] == 'e' or s[i] == 'E' or s[i] == 'i' or s[i] == 'I' or s[i] == 'o' or s[i] == 'O'or s[i] == 'u' or s[i] == 'U'):
                output += vowels[index]
                index += 1
            else:
                output += s[i]
        
        return output
        
def main():
    #print("Hello World!")
    test = Solution
    print(test.reverseVowels(test, "hello"))

if __name__ == "__main__":
    main()