import time

from Lab6.Downloader import Downloader


class SimpleDownloader(Downloader):
    def download(self, url):
        print(f"Downloading from {url}...")
        time.sleep(2)  # Імітуємо час завантаження
        return f"Data from {url}"
