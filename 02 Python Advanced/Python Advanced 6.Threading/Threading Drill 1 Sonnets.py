from threading import Thread, RLock
import os.path
lock = RLock()
class WriteSonnet(Thread):
    def __init__(self, text):
        Thread.__init__(self)
        self.text = text

    def run(self):
        path = os.path.abspath('/home/becode/data/ThreadSonnets')
        folder_path = path
        readFile = open(os.path.join(folder_path, self.text), "r") #merge path with self.text
        reading = readFile.read()
        with lock:
            #print(self.text)
            with open('/home/becode/data/ThreadSonnets/data_all.txt', 'a') as file:
                file.write(reading)
                file.write("\n") # new line between Sonnets
            file.close()

thread_1 = WriteSonnet("Sonnet_1")
thread_2 = WriteSonnet("Sonnet_2")
thread_3 = WriteSonnet("Sonnet_3")
thread_4 = WriteSonnet("Sonnet_4")
thread_5 = WriteSonnet("Sonnet_5")
thread_6 = WriteSonnet("Sonnet_6")
thread_7 = WriteSonnet("Sonnet_7")
thread_8 = WriteSonnet("Sonnet_8")
thread_9 = WriteSonnet("Sonnet_9")
thread_10 = WriteSonnet("Sonnet_10")

thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()
thread_5.start()
thread_6.start()
thread_7.start()
thread_8.start()
thread_9.start()
thread_10.start()

thread_10.join() # join or make sure all(or in this case maybe just the last) the threads finished reading and wrtiting before I print the final output file
f = open('/home/becode/data/ThreadSonnets/data_all.txt')
print(f.read())
f.close()

