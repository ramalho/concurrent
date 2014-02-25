//  Readers/Writers with concurrent read or exclusive write
//
// Usage:
//         javac rw.real.java
//         java Main rounds

class RWbasic {         // basic read or write
  protected int data = 0;  // the "database"
  protected void read() {
    System.out.println("read:  " + data);
  }
  protected void write() {
    data++;
    System.out.println("wrote:  " + data);
  }
}

class ReadersWriters extends RWbasic {  // Readers/Writers
  int nr = 0;
  private synchronized void startRead() {
    nr++;
  }
  private synchronized void endRead() {
    nr--;
    if (nr==0) notify();  // awaken waiting Writers
  }
  public void read() {
    startRead();
    System.out.println("read:  " + data);
    endRead();
  }
  public synchronized void write() {
    while (nr>0)
      try { wait(); } 
        catch (InterruptedException ex) {return;}
    data++;
    System.out.println("wrote:  " + data);
    notify();    // awaken another waiting Writer
  }
}
  
class Reader extends Thread {
  int rounds;
  ReadersWriters RW;
  public Reader(int rounds, ReadersWriters RW) {
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
  ReadersWriters RW;
  public Writer(int rounds, ReadersWriters RW) {
    this.rounds = rounds;
    this.RW = RW;
  }
  public void run() {
    for (int i = 0; i<rounds; i++) {
      RW.write();
    }
  }
}

class Main {  // driver program -- two readers and one writer
  static ReadersWriters RW = new ReadersWriters();
  public static void main(String[] arg) {
    int rounds = Integer.parseInt(arg[0],10);
    new Reader(rounds, RW).start();
    new Reader(rounds, RW).start();
    new Writer(rounds, RW).start();
  }
}
