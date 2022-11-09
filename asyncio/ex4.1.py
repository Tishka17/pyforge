import asyncio

# not working because Semaphore is created outside of running loop
semaphore = asyncio.Semaphore(5)


async def combine(a, b):
    print("combine", a, b)
    async with semaphore:
        await asyncio.sleep(1)
    print("combine done", a, b)
    return a + b


async def main():
    await asyncio.gather(*(
        combine(1, i)
        for i in range(20)
    ))


if __name__ == '__main__':
    asyncio.run(main())
