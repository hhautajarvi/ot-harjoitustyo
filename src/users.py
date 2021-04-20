from characters import Character
from repositories.user_repository import UserRepository

class Users:
    def __init__(self, name):
        self.name = name
        self.characterlist = {}

    def add_character(self, character: Character):
        self.characterlist[character.name] = character

    def give_characterlist(self):
        return self.characterlist


class Userlist:
    def __init__(self):
        self.user_repo = UserRepository("src/data/userfile.json")
        self.userlist = self.user_repo.load_users()

    def make_user(self, name):
        new_user = Users(name)
        self.userlist.append(name)
        self.user_repo.save_users(self.userlist)
        return new_user

    def give_userlist(self):
        return self.userlist
