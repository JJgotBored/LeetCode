class SmallestInfiniteSet:

    def __init__(self):
        self.removed = []
        return

    def popSmallest(self) -> int:
        smallest = 1
        for i in self.removed:
            if(i == smallest):
                smallest += 1
        self.removed.append(smallest)
        self.removed.sort()

        return smallest

    def addBack(self, num: int) -> None:
        for i in range(len(self.removed)):
            if(self.removed[i] == num):
                self.removed.pop(i)
                self.removed.sort()
                break

        return 
    
def main():
    test = SmallestInfiniteSet()

if(__name__ == "__main__"):
    main()