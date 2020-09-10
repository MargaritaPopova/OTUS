import csv
import asyncio
import sqlite3
from loguru import logger


async def read_csv():
    logger.info('Starting [read_csv]')
    with open('users.csv') as f:
        reader = csv.reader(f)
        count = 0
        for row in reader:
            if count == 0:
                header = '  ||  '.join(row)
                print(header)
                print('-'*len(header))
            else:
                print('  '.join(row))
            count += 1
    await asyncio.sleep(3)
    logger.info('Finishing [read_csv]')


async def second():
    logger.info('Starting [second]')
    print('second function')
    await asyncio.sleep(5)
    logger.info('Finishing [second]')


async def third():
    logger.info('Starting [third]')
    print('third function')
    await asyncio.sleep(10)
    logger.info('Finishing [third]')


def main():
    logger.info("Starting main")
    coroutines = [
        read_csv(),
        second(),
        third()
    ]
    coroutine = asyncio.wait(coroutines)
    asyncio.run(coroutine)
    logger.info("Finishing main")


if __name__ == '__main__':
    main()
