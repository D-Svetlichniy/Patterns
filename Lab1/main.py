from Lab1.StorageManager import StorageManager

manager = StorageManager()

# Для користувача "user1" використовуємо локальне сховище
user1_storage = manager.get_storage("user1", "local")
user1_storage.upload_file("example1.txt", b"Hello, Local World!")
user1_storage.download_file("example1.txt")

# Для користувача "user2" використовуємо сховище Amazon S3
user2_storage = manager.get_storage("user2", "s3")
user2_storage.upload_file("example2.txt", b"Hello, S3 World!")
user2_storage.download_file("example2.txt")