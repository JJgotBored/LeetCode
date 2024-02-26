class SmallestInfiniteSet:

    def __init__(self):
        self.removed = {}
        return

    def popSmallest(self) -> int:
        smallest = 1
        for i in range(1,len(self.removed.keys())+1):
            #print(i)
            if(smallest in self.removed.keys()):
                smallest += 1
        self.removed[smallest] = True
        #print(self.removed)

        return smallest

    def addBack(self, num: int) -> None:
        if(num in self.removed.keys()):
            self.removed.pop(num)

        #print(self.removed)
        return 
    
def main():
    test = SmallestInfiniteSet()
    print(test.addBack(2))
    print(test.popSmallest())
    print(test.popSmallest())
    print(test.popSmallest())
    print(test.addBack(1))
    print(test.popSmallest())
    print(test.popSmallest())
    print(test.popSmallest())


if(__name__ == "__main__"):
    main()