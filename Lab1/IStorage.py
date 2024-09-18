from abc import ABC, abstractmethod

class IStorage(ABC):                   #Визначає методи для роботи з файлами
    @abstractmethod
    def upload_file(self, file_name: str, data: bytes):
        pass

    @abstractmethod
    def download_file(self, file_name: str) -> bytes:
        pass

    @abstractmethod
    def delete_file(self, file_name: str):
        pass
