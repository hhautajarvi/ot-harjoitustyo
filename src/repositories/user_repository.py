import json

class UserRepository:
    def __init__(self, file):
        self.file = file

    def save_users(self, users: list):
        with open(self.file, "w") as jsonfile:
            data = {"userlist": users}
            json.dump(data, jsonfile)

    def load_users(self):
        with open(self.file) as jsonfile:
            file = jsonfile.read()
        data = json.loads(file)
        return data["userlist"]