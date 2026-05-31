from typing import Any

# Duck Typing - Simple & Flexible
def save_data(storage:Any):
    storage.save("data")  # Works with ANYTHING that has save()

# ✅ Works with database
class Database:
    def save(self, data: Any): 
        print(f"Saved to database: {data}")

# ✅ Works with file
class FileStorage:
    def save(self, data: Any): 
        print(f"Saved to file: {data}")

# ✅ Works with cloud
class CloudStorage:
    # def save(self, data: Any): 
    #     print(f"Saved to cloud: {data}")

    def nothing_method(self):
        print("Nothing to show")
        

# All work without inheritance or interfaces!
save_data(Database())
save_data(FileStorage())
save_data(CloudStorage())