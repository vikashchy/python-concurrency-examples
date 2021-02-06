from threading import Thread, Lock, Semaphore


class Bookbus:

    def __init__(self, availableseat):
        self.availableseat = availableseat
        self.l = Lock()                      # using locking
        # self.l = Semaphore()                 # using Sepaphore

    def bookseat(self, requestedseat):
        self.l.acquire()
        print("Total Seats available:", self.availableseat)
        if requestedseat <= self.availableseat:
            print("query seat")
            print("process payment")
            print("bookseat")
            self.availableseat -= requestedseat
            print("Total Seats left:", self.availableseat)
        else:
            print("No seats available")
        self.l.release()


ticket = Bookbus(10)
t1 = Thread(target=ticket.bookseat, args=(3,))
t2 = Thread(target=ticket.bookseat, args=(5,))
t3 = Thread(target=ticket.bookseat, args=(7,))

t1.start()
t2.start()
t3.start()
