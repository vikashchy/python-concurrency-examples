from threading import Thread, Lock, Semaphore, Condition
from time import sleep


class Producer:

    def __init__(self):
        self.products = []
        self.cond = Condition()

    def produce(self):
        self.cond.acquire()
        for i in range(1, 10):
            self.products.append("Product"+str(i))
            sleep(1)
            print("item added",str(i))
        self.cond.notify()
        self.cond.release()


class Consumer:
    def __init__(self, product):
        self.product = product

    def consume(self):
        self.product.cond.acquire()
        self.product.cond.wait(timeout=0)   # time to wait before executing the function/work
        self.product.cond.release()
        print("productshipped", self.product.products)


p = Producer()
c = Consumer(p)
t1 = Thread(target=p.produce).start()
t2 = Thread(target=c.consume).start()


