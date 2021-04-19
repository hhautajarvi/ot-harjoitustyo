from characters import Character


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
        self.userlist = []

    def make_user(self, name):
        new_user = Users(name)
        self.userlist.append(new_user)
        return new_user

    def give_userlist(self):
        return self.userlist
