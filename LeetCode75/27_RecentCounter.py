class RecentCounter:

    def __init__(self):
        self.queue = []

    def ping(self, t: int) -> int:
        self.queue.append(t)
        while((t - self.queue[0]) > 3000):
            self.queue.pop(0)
        return len(self.queue)

def main():
    test = RecentCounter()
    print(test.ping(1))
    print(test.ping(100))
    print(test.ping(3001))
    print(test.ping(3002))

if(__name__ == "__main__"):
    main()