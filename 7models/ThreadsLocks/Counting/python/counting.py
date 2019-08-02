import threading
import time


def main():
    class Counter:
        def __init__(self):
            self.count = 0

        def increment(self):
            temp = self.count
            time.sleep(0)
            self.count = temp + 1

    counter = Counter()

    def run():
        for x in range(10_000):
            counter.increment()

    t1 = threading.Thread(target=run)
    t2 = threading.Thread(target=run)

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print(counter.count)


main()
