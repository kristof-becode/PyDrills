from threading import Thread, RLock

lock = RLock()
class SyncThread(Thread):
    def __init__(self, text):
        Thread.__init__(self)
        self.text = text

    def run(self):
        with lock:
            print(self.text)
            with open('/home/becode/data/synch_thread.txt', 'a') as file:
                file.write(self.text)


#  We import RLock from the threading module
# We create a lock that we put into our lock variable
# In our run method, we lock part of our thread.

thread_1 = SyncThread("Thread 1 /")
thread_2 = SyncThread("Thread 2 /")
thread_3 = SyncThread("Thread 3 /")
thread_4 = SyncThread("Thread 4 /")

thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()

f = open('/home/becode/data/synch_thread.txt')
print(f.read())

