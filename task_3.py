import json
import threading

import requests


def fetch_url(_url, result_list):
    try:
        result = requests.get(_url)
        result_list.append((_url, result.text))
    except Exception as e:
        result_list.append((_url, f"Error: {str(e)}"))


if __name__ == "__main__":
    urls = [
        "https://fakestoreapi.com/products/1",
        "https://fakestoreapi.com/products/2",
        "https://fakestoreapi.com/products/3",
    ]
    responses = []

    threads = []
    for url in urls:
        thread = threading.Thread(target=fetch_url, args=(url, responses))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    with open("products.json", "w", encoding="utf-8") as json_file:
        json.dump(responses, json_file, indent=4)
