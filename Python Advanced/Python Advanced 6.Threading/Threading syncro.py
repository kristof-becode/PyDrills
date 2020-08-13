from threading import Thread

class MyThread(Thread):
    def __init__(self, text):
        Thread.__init__(self)
        self.text = text

    def run(self):
        print(self.text)
        with open('/home/becode/data/first_thread.txt', 'a') as file:
            file.write(self.text)


thread_1 = MyThread("My First thread! ")
thread_2 = MyThread("My Second thread! ")
thread_3 = MyThread("My third thread! ")
thread_4 = MyThread("My 4e thread! ")

thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()


f = open("/home/becode/data/first_thread.txt")
print(f.read())


