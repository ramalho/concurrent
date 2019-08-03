# Experiments with broken `DiningPhilosphers`

Running `DiningPhilosphers` (as written by Paul Butcher) several times, I never saw the `Philosopher.thinkCount` instance variable go beyond 200 before deadlocking.

However, removing the condition that makes the progress report `thinkCount` only in multiples of 10, I observed it go up to 1685 in one case:  

```
$ java com.paulbutcher.DiningPhilosophers 
...
Philosopher Thread[Thread-4,5,main] has thought 1679 times
Philosopher Thread[Thread-3,5,main] has thought 1672 times
Philosopher Thread[Thread-2,5,main] has thought 1684 times
Philosopher Thread[Thread-1,5,main] has thought 1664 times
Philosopher Thread[Thread-0,5,main] has thought 1676 times
Philosopher Thread[Thread-4,5,main] has thought 1680 times
Philosopher Thread[Thread-2,5,main] has thought 1685 times
Philosopher Thread[Thread-3,5,main] has thought 1673 times
Philosopher Thread[Thread-3,5,main] has thought 1674 times
Philosopher Thread[Thread-1,5,main] has thought 1665 times
Philosopher Thread[Thread-0,5,main] has thought 1677 times
Philosopher Thread[Thread-2,5,main] has thought 1686 times
Philosopher Thread[Thread-4,5,main] has thought 1681 times
Philosopher Thread[Thread-1,5,main] has thought 1666 times
Philosopher Thread[Thread-3,5,main] has thought 1675 times
Philosopher Thread[Thread-0,5,main] has thought 1678 times
Philosopher Thread[Thread-4,5,main] has thought 1682 times
Philosopher Thread[Thread-2,5,main] has thought 1687 times
Philosopher Thread[Thread-3,5,main] has thought 1676 times
Philosopher Thread[Thread-1,5,main] has thought 1667 times
Philosopher Thread[Thread-0,5,main] has thought 1679 times
Philosopher Thread[Thread-4,5,main] has thought 1683 times
Philosopher Thread[Thread-3,5,main] has thought 1677 times
Philosopher Thread[Thread-2,5,main] has thought 1688 times
Philosopher Thread[Thread-1,5,main] has thought 1668 times
Philosopher Thread[Thread-0,5,main] has thought 1680 times
Philosopher Thread[Thread-4,5,main] has thought 1684 times
Philosopher Thread[Thread-3,5,main] has thought 1678 times
Philosopher Thread[Thread-2,5,main] has thought 1689 times
Philosopher Thread[Thread-1,5,main] has thought 1669 times
Philosopher Thread[Thread-0,5,main] has thought 1681 times
Philosopher Thread[Thread-4,5,main] has thought 1685 times
```

Later I added a `toString` method to `Philosopher`, to make the output easier to read. Here is a sample run reporting `thinkCount` only in multiples of 10, deadlocking after 20:

```
$ java com.paulbutcher.DiningPhilosophers 
Philosopher #1 has thought 10 times
Philosopher #0 has thought 10 times
Philosopher #3 has thought 10 times
Philosopher #4 has thought 10 times
Philosopher #2 has thought 10 times
Philosopher #4 has thought 20 times
Philosopher #0 has thought 20 times
Philosopher #3 has thought 20 times
Philosopher #2 has thought 20 times
```
