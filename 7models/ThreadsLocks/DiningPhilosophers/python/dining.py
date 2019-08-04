import random
import time
import threading

MAX_DELAY = 10  # milliseconds

EAT_GOAL = 1000


class Philosopher:
    def __init__(self, number: int, left, right: threading.Lock) -> None:
        self.number = number
        self.first = left
        self.second = right
        threading.Thread(target=self.dine).start()

    def __str__(self):
        return f'Philosopher #{self.number}'

    def delay(self):
        # time.sleep(random.random() * MAX_DELAY / 1000)  # Hi-res delay
        time.sleep(random.randrange(MAX_DELAY) / 1000)  # Lo-res delay

    def dine(self):
        eat_count = 0
        while eat_count < EAT_GOAL:
            self.delay()  # Think for a while
            with self.first:  # Take first chopstick
                time.sleep(0)  # Hesitate
                with self.second:  # Take second chopstick
                    self.delay()  # Eat for a while
                    eat_count += 1
            if eat_count % 10 == 0:
                print(f'{self} has eaten {eat_count} times.')
        print(f'{self} is full.')


def main() -> None:
    chopsticks = [threading.Lock() for i in range(5)]

    for i in range(5):
        Philosopher(i, chopsticks[i], chopsticks[(i + 1) % 5])


main()
