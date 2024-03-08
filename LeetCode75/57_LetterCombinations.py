class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if(digits == ""):
            return []
        return []
    
    def recCombinations(self, digits: int, combo: list[str], depth: int, maxDepth: int, out: list[str]):
        if(depth == maxDepth):
            out.append(combo)
            return
        
        match digits[depth]:
            case 2:
                #a
                combo.append('a')
                self.recCombinations(digits, combo, depth+1, maxDepth, out)
                combo.pop(depth)
                #b
                combo.append('b')
                self.recCombinations(digits, combo, depth+1, maxDepth, out)
                combo.pop(depth)
                #c
                combo.append('c')
                self.recCombinations(digits, combo, depth+1, maxDepth, out)
                combo.pop(depth)

            case 3:
                combo.append('d')
            case 4:
                combo.append('g')
            case 5:
                combo.append('j')
            case 6:
                combo.append('m')
            case 7:
                combo.append('p')
            case 8:
                combo.append('t')
            case 9:
                combo.append('w')


        return
    
def main():
    test = Solution()

if(__name__ == "__main__"):
    main()
        