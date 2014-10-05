import threading
import sys
import time
import os

def snooze(duration):
    time.sleep(duration)


def main():
    if len(sys.argv) == 2:
        qt_threads = int(sys.argv[1].replace('k','000'))
    else:
        qt_threads = 100

    duration = 15

    for i in range(qt_threads):
        sleeper = threading.Thread(target=snooze, args=(duration,))
        sleeper.start()

    print('process id:', os.getpid())
    print('active threads:', threading.active_count())
    print()
    print('top -l1 -stats pid,th -pid ', os.getpid())
    while duration:
        print(duration, end=' ')
        sys.stdout.flush()
        time.sleep(1)
        duration -= 1

if __name__=='__main__':
    main()
