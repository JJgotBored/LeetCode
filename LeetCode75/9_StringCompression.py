class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        count = 0
        char = chars[0]
        comp = ""
        l = len(chars)

        for i in range(l):
            if(chars[i] == char):
                count += 1
            else:
                comp += char
                if(count > 1):
                    comp += str(count)
                char = chars[i]
                count = 1

            if(i == l-1):
                comp += char
                if(count > 1):
                    comp += str(count)
        chars[:] = comp
        return len(chars)    

def main():
    test = Solution
    print(test.compress(test, ["a","a","b","b","c","c","c"]))

if(__name__ == "__main__"):
    main()