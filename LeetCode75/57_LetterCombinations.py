class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if(digits == ""):
            return []
        
        digiList = []
        for i in list(digits):
            digiList.append(int(i)) 
        n = len(digiList)
        out = []
        #print(digiList, n)
        self.recCombinations(digiList, [], 0, n, out)
        #print(out)
        return out
    
    def recCombinations(self, digits: int, combo: list[str], depth: int, maxDepth: int, out: list[str]):
        if(depth == maxDepth):
            #print(combo)
            temp = ''.join(combo)
            #temp.join(combo)
            #print(temp)
            out.append(temp)
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
                #d
                combo.append('d')
                self.recCombinations(digits, combo, depth+1, maxDepth, out)
                combo.pop(depth)
                #e
                combo.append('e')
                self.recCombinations(digits, combo, depth+1, maxDepth, out)
                combo.pop(depth)
                #f
                combo.append('f')
                self.recCombinations(digits, combo, depth+1, maxDepth, out)
                combo.pop(depth)

            case 4:
                #g
                combo.append('g')
                self.recCombinations(digits, combo, depth+1, maxDepth, out)
                combo.pop(depth)
                #h
                combo.append('h')
                self.recCombinations(digits, combo, depth+1, maxDepth, out)
                combo.pop(depth)
                #i
                combo.append('i')
                self.recCombinations(digits, combo, depth+1, maxDepth, out)
                combo.pop(depth)

            case 5:
                #j
                combo.append('j')
                self.recCombinations(digits, combo, depth+1, maxDepth, out)
                combo.pop(depth)
                #k
                combo.append('k')
                self.recCombinations(digits, combo, depth+1, maxDepth, out)
                combo.pop(depth)
                #l
                combo.append('l')
                self.recCombinations(digits, combo, depth+1, maxDepth, out)
                combo.pop(depth)

            case 6:
                #m
                combo.append('m')
                self.recCombinations(digits, combo, depth+1, maxDepth, out)
                combo.pop(depth)
                #n
                combo.append('n')
                self.recCombinations(digits, combo, depth+1, maxDepth, out)
                combo.pop(depth)
                #o
                combo.append('o')
                self.recCombinations(digits, combo, depth+1, maxDepth, out)
                combo.pop(depth)

            case 7:
                #p
                combo.append('p')
                self.recCombinations(digits, combo, depth+1, maxDepth, out)
                combo.pop(depth)
                #q
                combo.append('q')
                self.recCombinations(digits, combo, depth+1, maxDepth, out)
                combo.pop(depth)
                #r
                combo.append('r')
                self.recCombinations(digits, combo, depth+1, maxDepth, out)
                combo.pop(depth)
                #s
                combo.append('s')
                self.recCombinations(digits, combo, depth+1, maxDepth, out)
                combo.pop(depth)

            case 8:
                #t
                combo.append('t')
                self.recCombinations(digits, combo, depth+1, maxDepth, out)
                combo.pop(depth)
                #u
                combo.append('u')
                self.recCombinations(digits, combo, depth+1, maxDepth, out)
                combo.pop(depth)
                #v
                combo.append('v')
                self.recCombinations(digits, combo, depth+1, maxDepth, out)
                combo.pop(depth)
            case 9:
                #w
                combo.append('w')
                self.recCombinations(digits, combo, depth+1, maxDepth, out)
                combo.pop(depth)
                #x
                combo.append('x')
                self.recCombinations(digits, combo, depth+1, maxDepth, out)
                combo.pop(depth)
                #y
                combo.append('y')
                self.recCombinations(digits, combo, depth+1, maxDepth, out)
                combo.pop(depth)
                #z
                combo.append('z')
                self.recCombinations(digits, combo, depth+1, maxDepth, out)
                combo.pop(depth)

        return
    
def main():
    digits = "2"
    test = Solution()
    print(test.letterCombinations(digits))

if(__name__ == "__main__"):
    main()
        