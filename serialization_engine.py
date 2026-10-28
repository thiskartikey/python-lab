import pickle
import shelve

class StudentRecord:
    def __init__(self, full_name, roll_id, score):
        self.full_name = full_name
        self.roll_id = roll_id
        self.score = score

    def show_info(self):
        print("Name:", self.full_name)
        print("Roll No:", self.roll_id)
        print("Marks:", self.score)


entry = StudentRecord("Kartikey Rajbhar", 241511, 92)

with open("student.pkl", "wb") as storage_file:
    pickle.dump(entry, storage_file)

print("Object saved using pickle.")

with open("student.pkl", "rb") as storage_file:
    loaded_entry = pickle.load(storage_file)

print("\nRestored object:")
loaded_entry.show_info()

with shelve.open("student_db") as db_store:
    db_store["record1"] = entry

print("\nObject saved using shelve.")

with shelve.open("student_db") as db_store:
    retrieved_entry = db_store["record1"]

print("\nObject retrieved from shelve:")
retrieved_entry.show_info()
