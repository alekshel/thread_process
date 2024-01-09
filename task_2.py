import concurrent.futures
import time


def calculate_sum(_nums):
    return sum(_nums)


def run_future(_executor, name, _nums):
    start_time = time.time()
    future = _executor.submit(calculate_sum, _nums)
    future.result()
    end_time = time.time()

    ex_time = round(end_time - start_time, 4)
    print(f"{name}: {ex_time} секунд")
    return ex_time


if __name__ == "__main__":
    _nums = list(range(1, 1000000))

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        threading_ex_time = run_future(executor, "Thread", _nums)

    with concurrent.futures.ProcessPoolExecutor(max_workers=2) as executor:
        process_ex_time = run_future(executor, "Process", _nums)

    if threading_ex_time < process_ex_time:
        print(
            "Thread швидше на: "
            + str(abs(threading_ex_time - process_ex_time))
            + " секунд"
        )
    else:
        print(
            "Process швидше на: "
            + str(abs(process_ex_time - threading_ex_time))
            + " секунд"
        )
