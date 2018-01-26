"""
Tests running short lived functions which in turn kick off longer lived "retry" functions
"""

import asyncio
import logging
import time
import uvloop

async def test(num, *args, **kwargs):
    logger = logging.getLogger('test {}'.format(num))
    logger.info('inside test - sleeping start')
    await asyncio.sleep(5)
    logger.info('inside test - sleeping end')
    return 'data'

async def schedule_test(loop, func, num, *args, **kwargs):
    logger = logging.getLogger('schedule_test {}'.format(num))

    async def _wrapper():
        logger.info('inside wrapper - sleeping start')
        await asyncio.sleep(5)
        logger.info('inside wrapper - sleeping end')
        return await func()

    try:
        await asyncio.wait_for(_wrapper(), 3, loop=loop)
    except asyncio.TimeoutError as e:
        logger.info('timeout error')
        await schedule_test(loop, func, num, *args, **kwargs)
        logger.info('new call')

async def run(loop, func, num):
    logger = logging.getLogger('run {}'.format(num))
    logger.info('calling schedule_test')
    asyncio.ensure_future(schedule_test(loop, func, num))
    logger.info('called schedule_test')
    return await func(num)

async def main():
    logger = logging.getLogger('main')
    futures = []
    for x in range(10):
        futures.append(asyncio.ensure_future(run(asyncio.get_event_loop(), test, x)))

    done, pending = await asyncio.wait(futures, return_when=asyncio.ALL_COMPLETED)
    for x in done:
        logger.info('run result: {}'.format(await x))

logging.basicConfig(level=logging.DEBUG)

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

loop = asyncio.get_event_loop()
asyncio.ensure_future(main())
loop.run_forever()
