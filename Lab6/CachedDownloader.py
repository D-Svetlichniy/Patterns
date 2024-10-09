from Lab6.Downloader import Downloader


class CachedDownloader(Downloader):
    def __init__(self, downloader):
        self.downloader = downloader
        self.cache = {}

    def download(self, url):
        if url in self.cache:
            print(f"Returning cached data for {url}")
            return self.cache[url]
        else:
            data = self.downloader.download(url)
            self.cache[url] = data
            return data
