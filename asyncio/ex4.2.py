import asyncio


async def combine(semaphore, a, b):
    print("combine", a, b)
    # this works similar to lock, but allow certain number of tasks
    # (limited by Semaphore value) to enter context at same time
    async with semaphore:
        await asyncio.sleep(1)
    print("combine done", a, b)
    return a + b


async def main():
    semaphore = asyncio.Semaphore(5)
    await asyncio.gather(*(
        combine(semaphore, 1, i)
        for i in range(20)
    ))


if __name__ == '__main__':
    asyncio.run(main())
