import concurrent.futures
import time

import requests


def _request(url):
    try:
        requests.get(url)
    except Exception as e:
        raise f"Error: {str(e)}"


if __name__ == "__main__":
    urls = ["https://openai.com/", "https://github.com/", "https://ithillel.ua/"]

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        start_time = time.time()

        futures = [executor.submit(_request, url) for url in urls]
        results = [future.result() for future in futures]

        end_time = time.time()
        threading_ex_time = round(end_time - start_time, 4)

    start_time = time.time()
    for _url in urls:
        _request(_url)
    end_time = time.time()
    liner_ex_time = round(end_time - start_time, 4)

    print(f"Thread: {threading_ex_time} секунд")
    print(f"Liner: {liner_ex_time} секунд")
