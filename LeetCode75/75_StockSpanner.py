class StockSpanner:

    def __init__(self):
        self.stack = []
        return

    def next(self, price: int) -> int:
        span = 1
        while(len(self.stack) > 0 and self.stack[0][0] <= price):
            span += self.stack[0][1]
            self.stack.pop(0)

        self.stack.insert(0,[price, span])

        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

def main():
    #print("Hello World")
    test = StockSpanner()
    inputs = [100, 80, 60, 70, 60, 75, 85]
    outputs = []

    for i in inputs:
        outputs.append(test.next(i))

    print(outputs)

if(__name__ == "__main__"):
    main()