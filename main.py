import asyncio

async def task(name, delay):
    print(f'{name} started')
    await asyncio.sleep(delay)
    print(f'{name} ended')

async def main():
    await asyncio.gather(
        task("Task1", 2),
        task('Task2', 1),
        task("Task3", 3),
    )

asyncio.run(main())