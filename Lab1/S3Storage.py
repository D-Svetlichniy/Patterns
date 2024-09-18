from Lab1.IStorage import IStorage


class S3Storage(IStorage):         #Клас для Amazon S3
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(S3Storage, cls).__new__(cls)
        return cls._instance

    def upload_file(self, file_name: str, data: bytes):
        # Для спрощення приклад не включає інтеграцію з S3 API
        print(f"File {file_name} uploaded to Amazon S3.")

    def download_file(self, file_name: str) -> bytes:
        # Симуляція завантаження з S3
        print(f"File {file_name} downloaded from Amazon S3.")
        return b"fake data from S3"

    def delete_file(self, file_name: str):
        print(f"File {file_name} deleted from Amazon S3.")
