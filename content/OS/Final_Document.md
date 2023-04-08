---
title: "Final Document"
draft: false
---

{{<toc>}}

# Processes
1. The kill bash command is used for
- [x] killing a process
- [ ] sending a signal to a process
- [ ] stopping a process
- [ ] resuming a process

2. When the shell has to execute a command (with its parameters) stored in a `char *argv[]` table, you can use:
- [ ] `execl()`
- [x] `execv()`
- [ ] `execlp()`
- [x] `execvp()`

3. In a Linux system, scheduling allows to execute
- [x] several processes on the same core
- [x] several processes on multiple cores
- [ ] only one process per core
- [ ] one process on multiple cores at the same time

4. The `fork()` function
- [ ] returns 0 to the father process
- [x] returns 0 to the child process
- [x] returns the pid of the child to the father process
- [ ] returns the pid of the child to the child process

5. After a call to `fork()`, the child process
- [ ] shares the address space of the father
- [x] has a copy of the address space of the father
- [x] has the same opened file descriptors as the father
- [ ] has no opened file descriptors

6. When we execute the following program :
```c
fork(); fork();
```
how many processes are created (including the one which executes the main())
- [ ] 3
- [x] 4
- [ ] 5
- [ ] 6

7. When we run an application `foo` (which takes 3 parameters from the command line) from a shell : `./foo p1 p2 p3`, in the main of the `foo` program, `argv` is:
- [ ] `{"p1", "p2", "p3"}`
- [x] `{"foo", "p1", "p2", "p3"}`
- [ ] `{"foo", "foo", "p1", "p2", "p3"}`

8. The `kill()` function
- [x] can be used to kill a process
- [x] can be used to send a signal
- [ ] can be used to remove a user
- [ ] can be used to shutdown the machine

# Schedule
1. The kill bash command is used for
- [x] killing a process
- [ ] sending a signal to a process
- [ ] stopping a process
- [ ] resuming a process

2. When the shell has to execute a command (with its parameters) stored in a `char *argv[]` table, you can use:
- [ ] `execl()`
- [x] `execv()`
- [ ] `execlp()`
- [x] `execvp()`

3. In a Linux system, scheduling allows to execute
- [x] several processes on the same core
- [x] several processes on multiple cores
- [ ] only one process per core
- [ ] one process on multiple cores at the same time

4. The `fork()` function
- [ ] returns 0 to the father process
- [x] returns 0 to the child process
- [x] returns the pid of the child to the father process
- [ ] returns the pid of the child to the child process

5. After a call to `fork()`, the child process
- [ ] shares the address space of the father
- [x] has a copy of the address space of the father
- [x] has the same opened file descriptors as the father
- [ ] has no opened file descriptors

6. When we execute the following program:
```c
fork(); fork();
```
how many processes are created (including the one which executes the main())
- [ ] 3
- [x] 4
- [ ] 5
- [ ] 6

7. When we run an application `foo` (which takes 3 parameters from the command line) from a shell : `./foo p1 p2 p3`, in the main of the `foo` program, `argv` is:
- [ ] `{"p1", "p2", "p3"}`
- [x] `{"foo", "p1", "p2", "p3"}`
- [ ] `{"foo", "foo", "p1", "p2", "p3"}`
- [ ] `{"foo", "p1", "p2", "p3", "p4"}`

8. The `kill()` function
- [x] can be used to kill a process
- [x] can be used to send a signal
- [ ] can be used to remove a user
- [ ] can be used to shutdown the machine

# Synchronization
1. In the reader/writer synchronization scheme, when some processes are reading
- [ ] a new writer can write
- [x] a new writer cannot write
- [x] a new reader can read
- [ ] a new reader cannot read

2. In the reader/writer synchronization scheme, when a process is writing
- [ ] a new writer can write
- [x] a new writer cannot write
- [ ] a new reader can read
- [x] a new reader cannot read

3. With Posix monitors, when you call `pthread_cond_signal(&condition);`
- [ ] the next thread which calls `pthread_cond_wait()` on the condition will not block
- [x] one thread which is blocked on the condition is resumed
- [x] if no thread is blocked on the condition, nothing happens and the signal is lost
- [ ] all the threads which are blocked on the condition are resumed

4. With semaphores, the `P()` function
- [ ] suspends the calling process if the counter is positive
- [x] suspends the calling process if the counter is negative
- [ ] increments the counter
- [x] decrements the counter

5. In a Posix monitor, what happens if we don't use the mutex lock ?
- [ ] the executing thread can block
- [x] the shared data may become unconsistent
- [ ] we can have a deadlock
- [x] all the threads can access the shared data at the same time

6. In the prodcons labwork with the products and freeslots conditions
- [ ] possibly no threads are blocked on any of the two conditions
- [ ] possibly threads are blocked on both conditions
- [x] if threads are blocked, they are all blocked on the same condition
- [ ] a thread can block at the same time on both conditions

7. In the prodcons labwork, the buffer will be most of the time
- [ ] empty if we create more producer threads
- [x] full if we create more producer threads
- [x] empty if we create more consumer threads
- [ ] full if we create more consumer threads

8. In the prodcons labwork with the products and freeslots conditions, if I produce, I must:
- [ ] test if the buffer is empty
- [x] test if the buffer is full
- [x] possibly block on the freeslots condition
- [ ] possibly block on the products condition

# Memory
1. The LRU eviction strategy
- [ ] is used to make space available in main memory
- [x] is used to make space available on disk
- [ ] selects the pages which should be sent to disk
- [x] selects the pages which should be loaded from disk

2. When a page fault occurs
- [ ] this is because memory is full
- [x] this is because memory is empty
- [x] this is because the page is in memory
- [ ] this is because the page is not in memory

3. When a page fault occurs
- [ ] a page will always be loaded
- [x] a page will always be sent to disk
- [x] there will always be a LRU selection
- [ ] there will possibly be a LRU selection

4. When a page is selected by LRU for replacement
- [x] this page must be loaded in memory
- [ ] this page must be sent to disk

5. When a page is selected by LRU for replacement
- [ ] this page can still be accessed
- [x] this page must be invalidated in the page table

6. When a page fault occurs, if memory is not full
- [x] a page will be allocated in memory
- [ ] a LRU selection will be operated
- [x] a page will be loaded from disk
- [ ] a page will be sent to disk

7. the principle of the working-set is that
- [x] 90% of page accesses fit in 10% of the memory
- [ ] 10% of page accesses fit in 90% of the memory
- [ ] 10% of page accesses fit in 10% of the memory
- [ ] 90% of page accesses fit in 90% of the memory

8. The goal of the LRU page eviction strategy is to
- [ ] keep the working-set in memory
- [x] send the working-set to disk
- [ ] keep Least Recently Used pages in memory
- [ ] send Least Recently Used pages to disk

# References
- [OS_FINAL_DEMO.7z](./OS_FINAL_DEMO.7z)