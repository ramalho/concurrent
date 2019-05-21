//  Readers/Writers with parallel access
//
// Usage:
//         javac rw.parallel.java
//         java Main rounds
//

class RWbasic { // basic read or write; no exclusion
  protected int data = 0;  // the "database"
  protected void read() {
    System.out.println("read:  " + data);
  }
  protected void write() {
    data++;
    System.out.println("wrote:  " + data);
  }
}

class Reader extends Thread {
  int rounds;
  RWbasic RW;
  public Reader(int rounds, RWbasic RW) {
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
  RWbasic RW;
  public Writer(int rounds, RWbasic RW) {
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
  static RWbasic RW = new RWbasic();
  public static void main(String[] arg) {
    int rounds = Integer.parseInt(arg[0],10);
    new Reader(rounds, RW).start();
    new Writer(rounds, RW).start();
  }
}
