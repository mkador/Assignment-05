import json
import os

class Memory:
    def __init__(self, file_path="conversation.json"):
        self.file_path = file_path
        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as f:
                json.dump([], f)

    def add(self, role, message):
        history = self.get_history()
        history.append({"role": role, "message": message})
        with open(self.file_path, "w") as f:
            json.dump(history, f, indent=2)

    def get_history(self):
        if not os.path.exists(self.file_path) or os.path.getsize(self.file_path) == 0:
            return []  
        try:
            with open(self.file_path, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            with open(self.file_path, "w") as f:
                json.dump([], f)
            return []
