import asyncio


def myprint():
    print("myprint")


async def main():
    loop = asyncio.get_event_loop()
    print(loop)
    # loop has some usefull methods
    loop.call_later(2, myprint)
    await asyncio.sleep(4)
    print("done")


if __name__ == '__main__':
    asyncio.run(main())
