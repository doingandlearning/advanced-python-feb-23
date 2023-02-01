
import asyncio
from time import strftime, localtime


async def displayAfter(msg, delay):
	await asyncio.sleep(delay)
	now = strftime("%H:%M:%S", localtime())
	print(f"{now} {msg}")
	return 42

async def main():
	print("***Start of main***")
	counter = 0
	task1 = asyncio.create_task(displayAfter("Hei", 3))
	print(asyncio.all_tasks())
	print("Task 1 has started")
	while True:
		print(asyncio.current_task())
		if task1.done():
			print(task1.result())
			break
		else:
			cancel = input("Task not complete yet. Do you want to cancel?")
			if cancel == "y":
				print("Okie doke!")
				task1.cancel()
				break
			else:
				print("I'll wait another second and ask again!")
				print(task1)
				await asyncio.sleep(1)


	print("***End of main***")

asyncio.run(main())