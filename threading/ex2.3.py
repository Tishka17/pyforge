from multiprocessing.pool import ThreadPool
from time import sleep

# remove global state, pass param to control expected behavior

def do(counter):
    diff = 0
    print("begin")
    if counter < 1:
        sleep(2)
        diff = 1
    print("end")
    return diff


pool = ThreadPool(2)

counter = 0
for res in pool.map(do, [0, 1]):
    counter += res
print(counter)
