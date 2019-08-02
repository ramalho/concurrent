import threading
import time

def main():

    def run():
        time.sleep(0)
        print('Hello from new thread')

    my_thread = threading.Thread(target=run)
    my_thread.start()
    print('Hello from main thread')
    my_thread.join()


main()
