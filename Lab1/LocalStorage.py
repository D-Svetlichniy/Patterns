import os
from Lab1.IStorage import IStorage


class LocalStorage(IStorage):         #Клас для локального сховища
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(LocalStorage, cls).__new__(cls)
        return cls._instance

    def upload_file(self, file_name: str, data: bytes):
        with open(file_name, 'wb') as f:
            f.write(data)
        print(f"File {file_name} uploaded to local storage.")

    def download_file(self, file_name: str) -> bytes:
        with open(file_name, 'rb') as f:
            data = f.read()
        print(f"File {file_name} downloaded from local storage.")
        return data

    def delete_file(self, file_name: str):
        os.remove(file_name)
        print(f"File {file_name} deleted from local storage.")
