from threading import Thread
from time import sleep

# some bad function
# here we use global variable as a shared state
# in real code data can be shared in other ways
counter = 0


def do():
    global counter
    if counter < 1:
        sleep(0.00001)
        counter += 1


# single threaded
print("=== Single threaded ===")
counter = 0
do()
do()
# expected counter=1
print(counter)


print("=== Multithreaded ===")
counter = 0
t1 = Thread(target=do)
t2 = Thread(target=do)
t1.start()
t2.start()

t1.join()
t2.join()

# expected counter value is 1 or 2
print(counter)
