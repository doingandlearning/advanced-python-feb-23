
import asyncio
from time import strftime, localtime


async def displayAfter(msg, delay):
	await asyncio.sleep(delay)
	now = strftime("%H:%M:%S", localtime())
	print(f"{now} {msg}")
	return 42

async def work():
	print("***Start of main***")
	task2 = asyncio.create_task(displayAfter("Bye", 3))
	task1 = asyncio.create_task(displayAfter("Hei", 3))
	print("Task 1 has started")
	task3 =  asyncio.create_task(displayAfter("Bye", 30))
	print("Task 2 has started")
	print("Do sommit importatn1")
	await asyncio.gather(task1, task2, task3)
	print("***End of main***")

async def main():
	result = asyncio.create_task(work())
	print("this is after")
	await result

asyncio.run(main())


