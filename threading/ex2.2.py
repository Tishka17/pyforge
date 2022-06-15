from threading import Thread, Lock
from time import sleep

# some bad function
# here we use global variable as a shared state
# in real code data can be shared in other ways
counter = 0

# global Lock added here just for demonstration - do not use global variables
lock = Lock()


def do():
    global counter
    with lock:
        print("begin")
        if counter < 1:
            sleep(2)
            counter += 1
        print("end")


counter = 0
t1 = Thread(target=do)
t2 = Thread(target=do)
t1.start()
t2.start()

t1.join()
t2.join()

# expected counter=1 but actually calls are consequent
print(counter)
