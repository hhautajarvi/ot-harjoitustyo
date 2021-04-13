from characters import Character
from users import Users
import json

class CharacterRepository:
    def __init__(self, file):
        self.file = file

    def save_data(self, character: Character, user: Users):
        with open(self.file) as jsonfile:
            file = jsonfile.read()
        data = json.loads(file)
        if data[user.name] not in data: 
            data[user.name] = []
        data[user.name].append({
            "name": character.name,
            "dwclass": character.dwclass,
            "alignment": character.alignment,
            "race": character.race,
            "image": character.image,
            "stats": character.stats,
            "backstory": character.backstory,
            "looks": character.looks
        })
        with open(self.file, "w") as jsonfile:
            json.dump(data, jsonfile)

    def read_data(self, user: Users):
        with open(self.file, "r") as jsonfile:
            for character in jsonfile[user.name]:
                new_character = Character(character["name"], user.name)
                new_character.choose_class(character["dwclass"])
                new_character.choose_alignment(character["alignment"])
                new_character.choose_race(character["race"])
                new_character.load_stats(character["stats"])
                new_character.choose_backstory(character["backstory"])
                new_character.choose_looks(character["looks"])
                user.add_character(new_character)