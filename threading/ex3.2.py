from timeit import timeit

# remove sleep and increase stop value

START = 0
STOP = 1_000_000


def do(start, number):
    sum = 0
    for i in range(start, start + number):
        sum += i
    return sum


def sequential():
    return do(START, STOP)


number = 20
res = timeit("sequential()", globals=globals(), number=number)
print("sequential:", res)

STEP = 10_000


def parallel(pool):
    sum = 0
    parts = [(i, STEP) for i in range(START, STOP, STEP)]
    for res in pool.starmap(do, parts):
        sum += res
    return sum


res = timeit("parallel(pool)", globals=globals(), number=number,
             setup="pool=ThreadPool(2)")
print("2 parallel:", res)
res = timeit("parallel(pool)", globals=globals(), number=number,
             setup="pool=ThreadPool(5)")
print("4 parallel:", res)
res = timeit("parallel(pool)", globals=globals(), number=number,
             setup="pool=ThreadPool(10)")
print("8 parallel:", res)

# ThreadPool is not faster anymore because of GIL


# try process pool
res = timeit("parallel(pool)", globals=globals(), number=number,
             setup="pool=Pool(2)")
print("2 processes:", res)
res = timeit("parallel(pool)", globals=globals(), number=number,
             setup="pool=Pool(4)")
print("4 processes:", res)
res = timeit("parallel(pool)", globals=globals(), number=number,
             setup="pool=Pool(8)")
print("8 processes:", res)
# ProcessPool is faster because there are no locks between cocurrent tasks
