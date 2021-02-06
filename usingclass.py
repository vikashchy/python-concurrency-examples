from threading import Thread, current_thread


class MyThread(Thread):

    def run(self, i=5):
        print(current_thread().getName())  # get name of the current thread
        for i in range(0, i):
            print(i)


mythread = MyThread()
mythread.start()
t1 = Thread(target=mythread.run, args=(2,))   # pass value to a function in thread target
t1.start()
t2 = Thread(target=mythread.run)
t2.start()
t3 = Thread(target=mythread.run)
t3.start()
