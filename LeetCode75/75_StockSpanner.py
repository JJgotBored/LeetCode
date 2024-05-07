class StockSpanner:

    def __init__(self):
        self.stack = []
        self.length = 0
        return

    def next(self, price: int) -> int:
        temp = 0

        if(self.length == 0 ):
            self.stack.append(price)
            self.length += 1
            return 1
        else:
            temp = 1
            for i in self.stack:
                if(price >= i):
                    temp += 1
                else:
                    break
            self.stack.insert(0, price)
            self.length += 1
            return temp
        return 0


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

def main():
    print("Hello World")
    test = StockSpanner()

if(__name__ == "__main__"):
    main()