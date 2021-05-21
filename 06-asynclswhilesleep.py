from asyncio import sleep, create_subprocess_exec, get_event_loop, gather
from pathlib import Path


async def async_sleep():
    val = await sleep(5.0, 5)
    print('after sleep. yawn')
    return val


sleep_coro = async_sleep()
subprocess_coro = create_subprocess_exec('ls', Path.home())
# asyncio.gather can be used to run multiple coroutines in parallel
# EventLoop.run_until_complete with multiple coroutines will run in sequence.
# It will run the first passed coroutine until an await is encountered. There a new thread or process will be created
# depending on the future we await on
# Then it will do the same for the second passed coroutine.
# Afterward it will check both coroutines until they can resume operation and will resume operation on the first
# that becomes available.
# Again, it will run until the next await or return
# When both coroutine is finished run_until_complete will return the result of the coroutines in a list
run_result = get_event_loop().run_until_complete(gather(sleep_coro, subprocess_coro))

print(run_result)
