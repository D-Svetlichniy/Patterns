from Lab1.StorageManager import user1_storage, user2_storage

# Для користувача "user1" використовується локальне сховище
user1_storage.upload_file("example.txt", b"Hello, World!")
user1_storage.download_file("example.txt")

# Для користувача "user2" використовується сховище Amazon S3
user2_storage.upload_file("example.txt", b"Hello, from S3!")
user2_storage.download_file("example.txt")
