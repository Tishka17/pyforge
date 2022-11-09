import asyncio


async def combine(a, b):
    print("combine", a, b)
    return a + b


async def main():
    res = combine(1, 2)
    print("Res", res)
    # use await to get result from awaitable like coroutine
    print("Res", await res)
    # this is also available
    res = await combine(1, 2)


if __name__ == '__main__':
    asyncio.run(main())


# normal function can return awaitable object as well if it calls async
# normal function cannot call await
def sync(a, b):
    res = combine(a, b)
    print("sync", res)
    return res
    # this is not allowed: return await res
