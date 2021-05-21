from asyncio import get_event_loop
import threading

# async is just syntantic sugar that changes a function's return type to a coroutine
# async functions runs on the callers thread, not on a separate thread
async def async_get_number() -> int:
    print(f'thread of async call {threading.current_thread()}')
    return 10

number = async_get_number()
print(number)
print(threading.current_thread())
# An event loop is required to run coroutines
print(get_event_loop().run_until_complete(number))
