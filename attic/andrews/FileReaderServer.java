// Simple server that reads a file and sends it back to a client.

// usage:
//   javac FileReaderServer.java
//   java FileReaderServer

import java.io.*;
import java.net.*;

public class FileReaderServer {
  public static void main(String args[]) {
    try {
      // create server socket to listen for connection on port 9999
      ServerSocket listen = new ServerSocket(9999);

      while (true) {
        System.out.println("server waiting for connection");
        Socket socket = listen.accept();  // wait for a client
        // create input and output streams to talk to client
        BufferedReader from_client =
          new BufferedReader(new InputStreamReader(socket.getInputStream()));
        PrintWriter to_client = new PrintWriter(socket.getOutputStream());

        // get filename from client and check if it exists
        String filename = from_client.readLine();
        File inputFile = new File(filename);
        if (!inputFile.exists()) {
          to_client.println("cannot open " + filename);
          to_client.close(); from_client.close();
          socket.close();
          continue;
        }

        // read lines from filename and send them to the client
        System.out.println("reading from file " + filename);
        BufferedReader input =
          new BufferedReader(new FileReader(inputFile));
        String line;
        while ((line = input.readLine()) != null)
          to_client.println(line);
        to_client.close(); from_client.close();
        socket.close();
      }
    }
    catch (Exception e) {  // report any exceptions
      System.err.println(e);
    }
  }
}
