import threading
import time

def show_time(interval):
    print ' '*int(70*interval)+time_strftime('%H:%M:%S.%m')
    time.sleep(interval)

my_thread = threading.Thread(target=say_hello)
my_thread.start()
# if delay is small (.001), output of newlines is non-deterministic
# time.sleep(.001)
print "Hello from main thread"
my_thread.join()
print "End of main"
