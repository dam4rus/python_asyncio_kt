from asyncio import get_event_loop, sleep


# async functions without an await is pointless since it will always run on the callers thread
async def async_get_number_after_five_seconds_invalid():
    # In an async function you have to "await" the result of other async functions to get it's result.
    # await is where execution will be yielded and other coroutines can be run by the event loop.
    val = await sleep(5.0, 5)
    print('after sleep. yawn')
    return val

number_coro = async_get_number_after_five_seconds_invalid()
print(get_event_loop().run_until_complete(number_coro))
