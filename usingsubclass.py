from threading import Thread, current_thread
from time import sleep


class MyThread:

    def display(self, i=5):
        print(current_thread().getName())
        for i in range(0, i):
            sleep(0.1)
            print(i)


mythread = MyThread()

t1 = Thread(target=mythread.display, args=(10,))   # pass value to a function in thread target
t1.start()

t2 = Thread(target=mythread.display)
t2.start()
t3 = Thread(target=mythread.display)
t3.start()
