/***
 * Excerpted from "Seven Concurrency Models in Seven Weeks",
 * published by The Pragmatic Bookshelf.
 * Copyrights apply to this code. It may not be used to create training material, 
 * courses, books, articles, and the like. Contact us if you are in doubt.
 * We make no guarantees that this code is fit for any purpose. 
 * Visit http://www.pragmaticprogrammer.com/titles/pb7con for more book information.
***/
import java.util.Random;

class Philosopher extends Thread {
  private int id;
  private Chopstick left, right;
  private Random random;
  private int eatCount;
  final int eatGoal = 50;

  public Philosopher(int id, Chopstick left, Chopstick right) {
    this.id = id;
    this.left = left; this.right = right;
    random = new Random();
  }

  public String toString() {
    return "Philosopher #" + id;
  }

  public void run() {
    try {
      while(eatCount < eatGoal) {
        Thread.sleep(random.nextInt(10));     // Think for a while
        synchronized(left) {                    // Grab left chopstick 
          synchronized(right) {                 // Grab right chopstick 
            Thread.sleep(random.nextInt(10)); // Eat for a while
          }
        }
        ++eatCount;
        if (eatCount % 10 == 0)
          System.out.println(this + " has eaten " + eatCount + " times.");
      }
      System.out.println(this + " is full.");

    } catch(InterruptedException e) {}
  }
}
