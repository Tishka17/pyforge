from multiprocessing.pool import ThreadPool
from time import sleep
from timeit import timeit

START = 0
STOP = 100


def do(start, number):
    sum = 0
    for i in range(start, start + number):
        sleep(0.001)
        sum += i
    return sum


# test sequential using timeit
def sequential():
    return do(START, STOP)


number = 20
res = timeit("sequential()", globals=globals(), number=number)
print("sequential:", res)

# test parallel variant
STEP = 10


def parallel(pool: ThreadPool):
    sum = 0
    parts = [(i, STEP) for i in range(START, STOP, STEP)]
    for res in pool.starmap(do, parts):
        sum += res
    return sum


assert sequential() == parallel(ThreadPool(5))

res = timeit("parallel(pool)", globals=globals(), number=number,
             setup="pool=ThreadPool(2)")
print("2 parallel:", res)
res = timeit("parallel(pool)", globals=globals(), number=number,
             setup="pool=ThreadPool(4)")
print("4 parallel:", res)
res = timeit("parallel(pool)", globals=globals(), number=number,
             setup="pool=ThreadPool(8)")
print("8 parallel:", res)

# look - it is much faster!