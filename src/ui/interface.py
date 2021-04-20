import sys
from characters import Character
from users import Userlist, Users
from repositories.character_repository import CharacterRepository


class Interface:
    def __init__(self):
        self.user_list = Userlist()
        self.character_load = CharacterRepository("src/data/characterfile.json")
        self.user_select()

    def user_select(self):
        print("Lopeta: 0")
        print("Tee uusi käyttäjä: 1")
        print("Valitse jokin valmis käyttäjä: 2")
        command = input("Anna komento: ")
        if command == "0":
            sys.exit()
        if command == "1":
            name = input("Anna käyttäjälle nimi: ")
            self.current_user = self.user_list.make_user(name)
            self.start()
        if command == "2":
            user_choice = self.user_list.give_userlist()
            for i in range(len(user_choice)):
                print(f"{user_choice[i]}: {i}")
            choice = int(input(
                "Valitse käyttäjä kirjoittamalla haluamasi käyttäjän numero: "))
            self.current_user = Users(user_choice[choice])
            self.character_load.read_data(self.current_user)
            self.start()

    def start(self):
        while True:
            self.instructions()
            command = input("Anna komento: ")
            if command == "0":
                break
            if command == "1":
                self.build_character()
            if command == "2":
                pass
            if command == "3":
                pass

    def instructions(self):
        print("Lopeta: 0")
        print("Tee uusi hahmo: 1")
        print("Pelaa ja muokkaa tekemääsi hahmoa: 2")
        print("Tee uusi hahmoluokka: 3")

    def build_character(self):
        name = input("Anna hahmolle nimi: ")
        if len(name) > 20 or len(name) < 1:
            while len(name) > 20 or len(name) < 1:
                name = input("Nimen pitää olla 1-20 merkkiä pitkä: ")
        self.new_character = Character(name)
        self.class_pick()
        self.alignment_pick()
        self.race_pick()
        self.stats_pick()
        backstory = input("Kerro hahmon taustatarina: ")
        self.new_character.choose_backstory(backstory)
        looks = input("Kuvaile hahmon ulkonäköä: ")
        self.new_character.choose_looks(looks)
        image = input("Anna hahmon kuvatiedoston osoite: ")
        self.new_character.choose_image(image)
        self.current_user.add_character(self.new_character)        
        self.character_load.save_data(self.new_character, self.current_user)

    def class_pick(self):
        while True:
            try:
                dw_class = int(input("Valitse luokka: 1: Bard, " \
                    "2: Barbarian, 3: Immolator, 4: Wizard, 5: Thief, 6: Ranger "))
                if 0 < dw_class < 7:
                    self.new_character.choose_class(dw_class)
                    break
            except:
                print("Anna kokonaisluku 1-6")

    def alignment_pick(self):
        while True:
            try:
                alignment = int(input("Valitse eettinen suuntaus. "
                                "1: Neutral, 2: Good, 3: Chaotic, 4: Evil, 5: Lawful "))
                if 0 < alignment < 6:
                    self.new_character.choose_alignment(alignment)
                    break
            except:
                print("Anna kokonaisluku 1-5")

    def race_pick(self):
        while True:
            try:
                race = int(input("Valitse rotu. 1: Human, 2: Dwarf, "
                "3: Elf, 4: Halfling 5: Salamander 6: Outsider "))
                if 0 < race < 7:
                    self.new_character.choose_race(race)
                    break
            except:
                print("Anna kokonaisluku 1-6")

    def stats_pick(self):
        while True:
            stats = [16, 15, 13, 12, 9, 8]
            try:
                print("Valitse hahmon taitopisteet. Mahdolliset taitotasot, "
              "valitse yksi jokaista: 16, 15, 13, 12, 9, 8")
                strength = int(input("Strength: "))
                dexterity = int(input("Dexterity: "))
                constitution = int(input("Constitution: "))
                intelligence = int(input("Intelligence: "))
                wisdom = int(input("Wisdom: "))
                charisma = int(input("Charisma: "))
                statlist = [strength, dexterity, constitution,
                            intelligence, wisdom, charisma]
                for stat in statlist:
                    if stat not in stats:
                        continue
                if sum(statlist) == sum(stats):
                    self.new_character.choose_stats(statlist)
                    break
                print("Annetut arvot eivät täsmää")
            except:
                print("Anna kokonaisluku")
