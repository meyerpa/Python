# Threads and Locks
**Single thread** process needs to switch between tasks to complete one process.
**Multithreading** each thread handles one tasks (threads)
+ *Note* each process has multiple threads
+ each thread shares same address space
+ Threads are lightweight in comparison the processes
**Multiprocessing**
+ Each process has different address space, so no global variables can be accessed
+ Benefit of multiprocess, if have memory leak in on process, won't affect other process.
+ In order to communicate with other processes, need shared memory

Both mutliprocessing and multithreading are ways to achieve multitasking.

## Threads in Python
When CPU on PC is idle, it allows the CPU to switch to another task.

`Python
t1 = threading.Thread(target=function, args=(funcarg1,))
t2 = threading.Thread(target=function2, args=(funcarg2,))

t1.start()    # start t1
t2.start()    # start t2

t1.join()     # wait until t1 is done
t2.join()     # wait until t2 is done
`

Multiprocessing in Python
`Python
def function(a, r):
  r[0] = 9

result = multiprocessing.Array('i', 3)
p1 = multiprocessing.Process(target = function, args=(arg1, result))
p2 = multiprocessing.Process(target = function, args=(arg2,))

p1.start()   # start process 1
p2.start()   # start process 2

p1.join()    # wait until process 1 finishes
p2.join()    # wait until process 2 finishes
`

# Locks in Python
`Python
def function(a, r, lock):
  lock.acquire()
  r[0] = 9
  lock.release()

result = multiprocessing.Array('i', 3)
lock = multiprocess.Lock()
p1 = multiprocessing.Process(target = function, args=(arg1, result, lock))
p2 = multiprocessing.Process(target = function, args=(arg2,))

p1.start()   # start process 1
p2.start()   # start process 2

p1.join()    # wait until process 1 finishes
p2.join()    # wait until process 2 finishes
`

## Multiprocessing Pool
**Map** separates data between units.
**Reduce** aggregates data from various units.
`Python
from multiprocessing import pool
p = Pool()
result = p.map(f, array)
p.close()
p.join()    # waits for all processes to finish
`

## Synchronization and Locks
Threads share same memory space
Pros
+ Allows threads to share data
Cons
+ Allows threads to modify a resource at the same time.
To prevent resource modification, we can use: atomic operations (rely only on one step), locks (wait for resource to be available to run operation)

### Re-Entrant Locks (R-Lock)
Blocks only if the lock is held by *another* thread.

### Semaphores
Have internal counter rather than a lock flag, and it only blocks if more than a given number of threads have attempted to hold the semaphore. This allows multiple threads to access same code section simultaneously.
`python
max_connections = 10
semaphore = threading.BoundedSemaphore(max_connections)
semaphore.acquire()
semaphore.release()
`

## Deadlocks and Deadlock Prevention
**Deadlock** is a situation where a thread is waiting for an object lock that another thread holds, and this second thread is waiting for an object lock that the first thread holds (or similarly with multiple threads).

In order for a deadlock to occur you must have all
1. Mutual Exclusion: Limited access to a resource
2. Hold and Wait: Processes holding resources can request additional resources
without relinquishing their current resources
3. No Preemption: one process cannot forcibly remove another process's resource
4. Circular Wait: Two or more processes from a circular chain where each
process is waiting on another resource in the chain.
To prevent deadlocks, remove any of the above conditions. But most focus on
removing number four, circular wait.
