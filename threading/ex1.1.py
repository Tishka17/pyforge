from threading import Thread
from time import sleep


def foo():
    print("begin")
    sleep(0.5)
    print("end")
    return "foo result"


# run function
print("=== Simple run ===")
print(foo())

# print function
print("=== Function object ===")
print(foo)

# create thread
print("=== Threading ===")
thread = Thread(target=foo)  # function intself, not function call!
print("thread created", thread)
thread.start()
print("thread started", thread)
# wait thread finished
thread.join()
print("thread finished", thread)
