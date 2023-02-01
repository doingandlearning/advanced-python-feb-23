# Import the concurrent.futures module, which provides an API for true parallel processing with results.
from concurrent.futures import ThreadPoolExecutor

import time
import threading


def display(msg):
    str = "[Thread {}: {} ".format(threading.get_ident(), msg)
    print(str)


def gimme_result_after(delay):
    display('Start of gimme_result')
    time.sleep(delay)
    display('End of gimme_result')
    return 42


if __name__ == '__main__':

    # Create a ThreadPoolExecutor with 5 worker threads, to do 5 things truly parallel.
    number_of_threads = 5
    threadpool = ThreadPoolExecutor(number_of_threads)

    # Submit a task to the threadpool. The threadpool will execute the task on a thread.
    future = threadpool.submit(gimme_result_after, 10)

    while True:
        if future.done():
            result = future.result()
            display('After all that, the result is ' + str(result))
            break
        else:
            display("Result not in yet, so I'll do something useful...")
            time.sleep(1)

    display('All done!')