from Lab1 import IStorage
from Lab1.LocalStorage import LocalStorage
from Lab1.S3Storage import S3Storage


class StorageManager:        #Менеджер сховищ
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(StorageManager, cls).__new__(cls)
            cls._storages = {}
        return cls._instance

    def get_storage(self, user_id: str, storage_type: str) -> IStorage:
        if user_id not in self._storages:
            if storage_type == "local":
                self._storages[user_id] = LocalStorage()
            elif storage_type == "s3":
                self._storages[user_id] = S3Storage()
            else:
                raise ValueError(f"Unsupported storage type: {storage_type}")
        return self._storages[user_id]
