public class HelloWorld {

  public static void main(String[] args) throws InterruptedException {
    Thread myThread = new Thread() {
        public void run() {
          try {
            Thread.sleep(1000);
          }
          catch (InterruptedException e) {}
          System.out.println("Hello from new thread");
        }
      };
    myThread.start();
    //Thread.sleep(1);
    System.out.println("Hello from main thread");
    //myThread.join();
    System.out.println("End of main");
  }
}
