from threading import Thread, current_thread


def display():
    i = 0
    print(current_thread().getName())
    while i <= 4:
        print(i)
        i += 1


mythread = Thread(target=display)
mythread.start()       # Start method spawns a new thread
# mythread.start       # Try create a new thread  -> Thread  cannot be started more than once.
# mythread.run()       # run method runs the target on the main thread
