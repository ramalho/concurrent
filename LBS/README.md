# The Little Book of Semaphores

This directory contains examples, exercises, and experiments based on Allen Downey's
[The Little Book of Semaphores](https://greenteapress.com/wp/semaphores/).


## Semaphore method names

Below are some semaphore method names mentioned by Prof. Downey in section 2.2,
and the names of the methods in Python's `threading.Semaphore` class (same as Java's
`concurrent.Semaphore` class) and [POSIX](https://linux.die.net/man/7/sem_overview).
    
| Dykstra | action      | used for | Python/Java | POSIX      | meaning
| ------- | ----------- | -------- | ----------- | ---------- | ------------
| **P**   | `decrement` | `wait`   | `acquire`   | `sem_wait` | decrement and block if the result is negative
| **V**   | `increment` | `signal` | `release`   | `sem_post` | increment and wake a waiting process if any