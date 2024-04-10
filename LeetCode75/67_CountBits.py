class Solution:
    def countBits(self, n: int) -> list[int]:
        out = []
        out.append(0)
        for i in range(1, n+1):
            if(i%2 == 0):
                out.append(out[i//2])
            else:
                out.append(out[i//2]+1)
        return out
    
def main():
    test = Solution()
    n = 5

    print(test.countBits(n))

if(__name__ == "__main__"):
    main()