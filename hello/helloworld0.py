"""
public class HelloWorld {

  public static void main(String[] args) throws InterruptedException {
    Thread myThread = new Thread() {
        public void run() {
          System.out.println("Hello from new thread");
        }
      };
    myThread.start();
    Thread.sleep(1);
    System.out.println("Hello from main thread");
    myThread.join();
  }
}
"""

import thread
import time

def say_hello():
    print 'Hello from new thread'

my_thread = thread.start_new_thread(say_hello, ())
# if delay is small (.001), output of newlines is non-deterministic
time.sleep(.001)
print "Hello from main thread"
