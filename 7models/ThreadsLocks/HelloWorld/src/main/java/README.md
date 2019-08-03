# The simplest way to run this example

To compile and run the `HelloWorld.java` example in page 10 of _Seven Concurrency Models in Seven Weeks_, run these commands from the directory where this `README.md` is located:

```
$ javac com/paulbutcher/HelloWorld.java
$ java com.paulbutcher.HelloWorld 
Hello from main thread
Hello from new thread
```

Simple and _just works™!_


## Why not Maven?

The bare-bones, old-fashioned way to compile and run Java programs works fine with the simple examples in chapter 1 of _Seven Concurrency Models in Seven Weeks_.

I tried to use Maven as the author recommended in `ThreadsLocks/README`, but I found it too complicated, `mvn` downloaded lots of stuff for no obvious reason, and the output of `mvn exec:java` has a lot of noise that obscures the simple output of the program. I bet there are command-line options to silece that, but I decided to go back to basics and use just `javac` and `java`.
