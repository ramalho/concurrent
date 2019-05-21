#!/usr/bin/env python3

"""
Allen's tasks:

1. Eat breakfast
2. Work
3. Eat lunch
4. Call Bob


Bob's tasks:

1. Eat breakfast
2. Wait for a call
3. Eat lunch
"""

import threading
import random
import time

from threading_cleanup import Thread


def show(name, activity):
    time.sleep(random.random() / 10)
    print(name, activity, sep=':\t', flush=True)


def allen(call):
    show('Allen', 'Eat breakfast')
    show('Allen', 'Work')
    show('Allen', 'Eat lunch')
    show('Allen', 'Call Bob')
    call.set()


def bob(call):
    show('Bob', 'Eat breakfast')
    show('Bob', 'Wait for a call')
    call.wait()
    show('Bob', 'Eat lunch')


def main():
    call = threading.Event()
    Thread(allen, call)
    Thread(bob, call)


main()