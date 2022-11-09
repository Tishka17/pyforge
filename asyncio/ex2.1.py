import asyncio
import time


async def combine(a, b):
    print("combine", a, b)
    # time.sleep is blocking whole tread end eventloop
    time.sleep(3)  # should be replaced with: await asyncio.sleep(1)
    print("combine done", a, b)
    return a + b


async def main():
    # no concurrency
    await combine(1, 2)
    await combine(3, 4)

    # concurrent (if replace `time.sleep` with `asyncio.sleep`)
    task1 = asyncio.create_task(combine(1, 2))
    task2 = asyncio.create_task(combine(1, 2))

    # We need to wait somehow until all tasks done
    await task1
    await task2
    # other option is to gather result from tasks
    # await asyncio.gather(task1, task2)

    # gather creates tasks implicitly, so this is allowed:
    # res = await asyncio.gather(
    #     combine(1, 2),
    #     combine(3, 4),
    # )
    # print(res)


if __name__ == '__main__':
    asyncio.run(main())
