# The Little Book of Semaphores

This directory contains examples, exercises, and experiments based on Allen Downey's
[The Little Book of Semaphores](https://greenteapress.com/wp/semaphores/).


## Semaphore method names

Below are some semaphore method names mentioned by Prof. Downey in section 2.2,
and the names of the methods in Python's `threading.Semaphore` class.
    
| Dykstra | action      | used for | Python     | meaning
| ------- | ----------- | -------- | ---------- | ------------
| **P**   | `decrement` | `wait`   | `acquire`  | decrement and block if the result is negative
| **V**   | `increment` | `signal` | `release`  | increment and wake a waiting process if any
