import asyncio
import time


def combine(a, b):
    print("combine", a, b)
    time.sleep(1)
    print("combine done", a, b)
    return a + b


async def main():
    # we can run classic blocking functions using Executor
    # None here means using default ThreadPoolExecutor
    res1 = asyncio.get_event_loop().run_in_executor(None, combine, 1, 2)
    res2 = asyncio.get_event_loop().run_in_executor(None, combine, 3, 4)
    print(res1)
    print(await res1)
    print(await res2)


if __name__ == '__main__':
    asyncio.run(main())
