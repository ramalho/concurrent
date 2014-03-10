
"""
saidas do original em Java:

The meaning of life is: 42
lontra:py luciano$ java Puzzle
The meaning of life is: 42
lontra:py luciano$ java Puzzle
The meaning of life is: 42
lontra:py luciano$ java Puzzle
I don't know the answer
lontra:py luciano$ java Puzzle
The meaning of life is: 42

Segundo o autor, pode acontecer tambem (mas eu nao vi):

The meaning of life is: 0
"""

from threading import Thread
from time import sleep

def f1():
    global answer, answer_ready
    answer = 42
    answer_ready = True

def f2():
    if answer_ready:
        print('The meaning of life is: %s' % answer)
    else:
        print("I don't know the answer")

while True:
    answer_ready = False
    answer = 0

    t1 = Thread(target=f1)
    t2 = Thread(target=f2)

    t1.start()
    t2.start()
    t1.join()
    t2.join()


