from typing import Protocol

class Storage(Protocol):
    def save(self, data:str) -> None:
        ...

# ✅ Works with database
class Database:
    def save(self, data:str) -> None: 
        print(f"Saved to database: {data}")

# ✅ Works with file
class FileStorage:
    def save(self, data:str): 
        print(f"Saved to file: {data}")

    def read_from_file_storage(self,data:str):
        print(f"Read data from: {data}")

# ✅ Works with cloud
class CloudStorage:
    def save(self, data:str): 
        print(f"Saved to cloud: {data}")

def save_data(storage:Storage):
    storage.save("data")  # Works with ANYTHING that has save()

# All work without inheritance or interfaces!
save_data(Database())
save_data(FileStorage())
save_data(CloudStorage())