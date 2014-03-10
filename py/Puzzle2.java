/***
 * Excerpted from "Seven Concurrency Models in Seven Weeks",
 * published by The Pragmatic Bookshelf.
 * Copyrights apply to this code. It may not be used to create training material,
 * courses, books, articles, and the like. Contact us if you are in doubt.
 * We make no guarantees that this code is fit for any purpose.
 * Visit http://www.pragmaticprogrammer.com/titles/pb7con for more book information.
***/

public class Puzzle {

  static boolean answerReady = false;
  static int answer = 0;

  Thread1 t1;
  Thread2 t2;

  class Thread1 extends Thread {
      public void run() {
        answer = 42;
        answerReady = true;
      }
    };

  class Thread2 extends Thread {
      public void run() {
        if (answerReady)
          System.out.println("The meaning of life is: " + answer);
        else
          System.out.println("I don't know the answer");
      }
    };

  public static void main(String[] args) throws InterruptedException {
    while (true) {
      t1 = new Thread1();
      t2 = new Thread2();
      t1.start(); t2.start();
      t1.join(); t2.join();
    }
  }
}
