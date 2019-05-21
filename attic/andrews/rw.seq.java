// a simple, unsynchronized database

// usage:
//    javac rw.seq.java  (this file)
//    java Main rounds


class RWbasic {  // basic read or write (no synchronization)
  protected int data = 0;  // the "database"

  public void read() {
    System.out.println("read:  " + data);
  }

  public void write() {
    data++;
    System.out.println("wrote:  " + data);
  }
}

class Main {  // driver program
  static RWbasic RW = new RWbasic();

  public static void main(String[] arg) {
    int rounds = Integer.parseInt(arg[0],10);
    for (int i = 0; i < rounds; i++) {
      RW.read();
      RW.write();
    }
  }
}
