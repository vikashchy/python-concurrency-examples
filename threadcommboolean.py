from threading import Thread, Lock, Semaphore
from time import sleep


class Producer:

    def __init__(self):
        self.products = []
        self.orderplaced = False

    def produce(self):
        for i in range(1, 10):
            self.products.append("Product"+str(i))
            sleep(1)
            print("item added")
        self.orderplaced = True


class Consumer:
    def __init__(self, product):
        self.product = product

    def consume(self):
        while not self.product.orderplaced:
            sleep(0.2)
        print("productshipped", self.product.products)


p = Producer()
c = Consumer(p)
t1 = Thread(target=p.produce).start()
t2 = Thread(target=c.consume).start()


