from asyncio import sleep, create_subprocess_exec, get_event_loop
from pathlib import Path


async def async_ls_after_sleep():
    val = await sleep(5.0, 5)
    print(f'after sleep. yawn {val}')
    # This will run after sleep. If you want functions to run parallel you have to use multiple coroutines
    await create_subprocess_exec('ls', Path.home())


ls_after_sleep_coro = async_ls_after_sleep()
get_event_loop().run_until_complete(ls_after_sleep_coro)
