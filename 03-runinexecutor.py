from asyncio import get_event_loop
from concurrent.futures import ThreadPoolExecutor
from threading import current_thread


def get_number() -> int:
    # Since get_number is wrapped in a future with a ThreadPoolExecutor it will run on a different thread
    print(f'thread of get_number {current_thread()}')
    return 5

# To create a future that runs on a separate thread or process you have to create it with EventLoop.run_in_executor
get_number_future = get_event_loop().run_in_executor(ThreadPoolExecutor(), get_number)
print(get_event_loop().run_until_complete(get_number_future))
