# 3. Multi-Threaded Downloader

## Code
import threading
import requests

url = "https://example.com/file.zip"


def download_file():
    response = requests.get(url)

    with open("downloaded_file.zip", "wb") as file:
        file.write(response.content)

    print("Download Completed")

thread = threading.Thread(target=download_file)
thread.start()
thread.join()