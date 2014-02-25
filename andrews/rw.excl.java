//  Readers/Writers with exclusive access.
//
// Usage:
//         javac rw.exclusive.java
//         java Main rounds

class RWbasic {         // basic read or write (data; no synch)
  protected int data = 0;  // the "database"
  protected void read() {
    System.out.println("read:  " + data);
  }
  protected void write() {
    data++;
    System.out.println("wrote:  " + data);
  }
}

class RWexclusive extends RWbasic {  // exclusive read and write
  public synchronized void read() {
    System.out.println("read:  " + data);
  }
  public synchronized void write() {
    data++;
    System.out.println("wrote:  " + data);
  }
}
  
class Reader extends Thread {
  int rounds;
  RWexclusive RW;
  public Reader(int rounds, RWexclusive RW) {
    this.rounds = rounds;
    this.RW = RW;
  }
  public void run() {
    for (int i = 0; i<rounds; i++) {
      RW.read();
    }
  }
}

class Writer extends Thread {
  int rounds;
  RWexclusive RW;
  public Writer(int rounds, RWexclusive RW) {
    this.rounds = rounds;
    this.RW = RW;
  }
  public void run() {
    for (int i = 0; i<rounds; i++) {
      RW.write();
    }
  }
}

class Main {  // driver program
  static RWexclusive RW = new RWexclusive();
  public static void main(String[] arg) {
    int rounds = Integer.parseInt(arg[0],10);
    new Reader(rounds, RW).start();
    new Writer(rounds, RW).start();
  }
}
