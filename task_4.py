import sys
import multiprocessing
from multiprocessing import Manager

import requests


def _request(url, results):
    try:
        result = requests.get(url)
        results[url] = result.text
    except Exception as e:
        results[url] = f"Error: {str(e)}"


if __name__ == "__main__":
    urls = ["https://openai.com/", "https://github.com/", "https://ithillel.ua/"]

    with Manager() as manager:
        results_dict = manager.dict()

        processes = []
        for _url in urls:
            process = multiprocessing.Process(
                target=_request, args=(_url, results_dict)
            )
            processes.append(process)
            process.start()

        for process in processes:
            process.join()

        for _url, response in results_dict.items():
            byte_size = sys.getsizeof(response)
            kilobyte_size = round(byte_size / 1024, 2)
            print(f"URL: {_url}, Текст: {kilobyte_size} кілобайт")
