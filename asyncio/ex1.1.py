import asyncio


# function which returns special object
def generator():
    yield 1
    yield 2


print(generator())  # generator object

# we can iterate over generator to execute it and retrieve contents
for i in generator():
    print(i)


# another function with special result
async def main():
    print("Hello, world")


print(main)
print(main())  # coroutine object

# we can run coroutine using asyncio to execute it
asyncio.run(main())
