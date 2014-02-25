// Get a file from RemoteFileServer and print it on stdout.

//  usage:
//    javac Client.java
//    java Client "hostname" "filename"  (after starting the server)

import java.io.*;
import java.net.*;

public class Client {
  public static void main(String[] args) {
    try {
      // read command-line arguments
      if (args.length != 2) {
        System.out.println("need 2 arguments");
        System.exit(1);
      }
      String host = args[0];
      String filename = args[1];

      // open socket, then input and output streams to it
      Socket socket = new Socket(host,9999);
      BufferedReader from_server = 
        new BufferedReader(new InputStreamReader(socket.getInputStream()));
      PrintWriter to_server = new PrintWriter(socket.getOutputStream());

      // send filename to server, then read and print lines until
      // the server closes the connection
      to_server.println(filename); to_server.flush();
      String line;
      while ((line = from_server.readLine()) != null) {
        System.out.println(line);
      }
    }
    catch (Exception e) {    // report any exceptions
      System.err.println(e);
    }
  }
}
