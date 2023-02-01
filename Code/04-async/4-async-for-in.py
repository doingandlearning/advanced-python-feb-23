
import asyncio
from time import strftime, localtime


async def displayAfter(msg, delay):
	await asyncio.sleep(delay)
	now = strftime("%H:%M:%S", localtime())
	print(f"{now} {msg}")
	return 42

async def main():
	print("***Start of main***")
	awaitables = [a async for  asyncio.create_task(displayAfter("Hello", 1))] * 10
	async for i in awaitables:
		print(i.result())



# define an asynchronous iterator
class AsyncIterator():
    # constructor, define some state
    def __init__(self):
        self.counter = 0
 
    # create an instance of the iterator
    def __aiter__(self):
        return self
 
    # return the next awaitable
    async def __anext__(self):
        # check for no further items
        if self.counter >= 10:
            raise StopAsyncIteration
        # increment the counter
        self.counter += 1
        # return the counter value
        return self.counter

	print("***End of main***")

asyncio.run(main())