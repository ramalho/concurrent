import random
import time
import threading

MAX_DELAY = 10  # milliseconds

EAT_GOAL = 10000


class Philosopher:
    def __init__(self, number: int, left, right: threading.Lock):
        self.number = number
        self.left = left
        self.right = right
        self.random = random.Random()
        self.eat_count = 0

    def __str__(self):
        return f'Philosopher #{self.number}'

    def delay(self):
        #time.sleep(self.random.random() * MAX_DELAY / 1000)  # Hi-res delay
        time.sleep(self.random.randrange(MAX_DELAY) / 1000)  # Lo-res delay

    def run(self):
        while self.eat_count < EAT_GOAL:
            self.delay()          # Think for a while
            with self.left:         # Take first chopstick
                with self.right:      # Take second chopstick
                    self.delay()        # Eat for a while
            self.eat_count += 1
            if self.eat_count % 10 == 0:
                print(f'{self} has eaten {self.eat_count} times.')
        print(f'{self} is full.')


def main():
    chopsticks = [threading.Lock() for i in range(5)]

    threads = []
    for i in range(5):
        p = Philosopher(i, chopsticks[i], chopsticks[(i + 1) % 5])
        t = threading.Thread(target=p.run)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()  # this will never happen because each thread is an infinite loop


main()
