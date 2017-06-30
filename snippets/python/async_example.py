#!/usr/bin/env python3

import asyncio


async def coroutine():
    print('in coroutine')
    return 'asd'

async def main():
    print('starting coroutine')
    routine = coroutine()
    print('entering event loop')
    val = await routine
    val2 = await coroutine()
    print(val2)
    print(val)
    print('exiting')


if __name__ == '__main__':
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(main())
    event_loop.close()
