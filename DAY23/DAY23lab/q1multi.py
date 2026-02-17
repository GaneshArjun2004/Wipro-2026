import requests
import threading
import time

urls = [
    "https://example.com/data1",
    "https://example.com/data2",
    "https://example.com/data3",
    "https://example.com/data4"
]

def download_file(url):
    try:
        response = requests.get(url)
        filename = url.split("/")[-1] + ".txt"

        with open(filename, "w", encoding="utf-8") as f:
            f.write(response.text)

        print(f"Downloaded: {filename}")

    except Exception as e:
        print(f"Error downloading {url}: {e}")

# ------------------ Sequential Download ------------------
start_time = time.time()

for url in urls:
    download_file(url)

sequential_time = time.time() - start_time
print(f"\nSequential download time: {sequential_time:.2f} seconds")

# ------------------ Threaded Download ------------------
start_time = time.time()

threads = []
for url in urls:
    t = threading.Thread(target=download_file, args=(url,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

threaded_time = time.time() - start_time
print(f"\nThreaded download time: {threaded_time:.2f} seconds")