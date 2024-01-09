import concurrent.futures


def print_even_nums(_limit):
    for i in range(2, _limit + 1, 2):
        print(f"Парні числа: {i}")


def print_odd_nums(_limit):
    for i in range(1, _limit + 1, 2):
        print(f"Не парні числа: {i}")


if __name__ == "__main__":
    _limit = 20

    with concurrent.futures.ProcessPoolExecutor() as executor:
        future_even = executor.submit(print_even_nums, _limit)
        future_odd = executor.submit(print_odd_nums, _limit)

        concurrent.futures.wait([future_even, future_odd])

        for future in [future_even, future_odd]:
            if future.exception() is not None:
                print(f"Exception: {future.exception()}")
