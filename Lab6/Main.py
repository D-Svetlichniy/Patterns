from Lab6.CachedDownloader import CachedDownloader
from Lab6.SimpleDownloader import SimpleDownloader

if __name__ == "__main__":
    downloader = SimpleDownloader()
    cached_downloader = CachedDownloader(downloader)

    # Перше завантаження - з сервера
    data1 = cached_downloader.download("https://example.com")
    print(data1)

    # Друге завантаження - з кешу
    data2 = cached_downloader.download("https://example.com")
    print(data2)
