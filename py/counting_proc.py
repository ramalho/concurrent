# Adapted from "Seven Concurrency Models in Seven Weeks",
# by Paul Butcher, published by The Pragmatic Bookshelf.

from multiprocessing import Process

class Counter:
    count = 0
    def increment(self):
        self.count += 1

counter = Counter()

def do_count():
    for i in range(10000):
        counter.increment()


t1 = Process(target=do_count)
t2 = Process(target=do_count)

t1.start()
t2.start()
t1.join()
t2.join()

print(counter.count)
