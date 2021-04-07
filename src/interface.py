import characters
from users import Users, Userlist

class Interface:
    def __init__(self):
        Userlist()
        self.user_select()

    def user_select(self):
        print("Lopeta: 0")
        print("Tee uusi käyttäjä: 1")
        print("Valitse jokin valmis käyttäjä: 2")
        command = input("Anna komento: ")
        if command == "0":
            quit()
        if command == "1":
            name = input("Anna käyttäjälle nimi: ")
            current_user = Userlist.make_user(name)
            self.start(current_user)
        if command == "2":
            user_choice = Userlist.give_userlist()
            for i in range(len(user_choice)-1):
                print(f"{user_choice[0]}: {i}")
            choice = input("Valitse käyttäjä kirjoittamalla haluamasi käyttäjän numero: ")
            self.start(user_choice[choice])

    def start(self, user):
        self.instructions()
        while True:
            command = input("Anna komento: ")
            if command == "0":
                break
            if command == "1":
                new_character = characters.make_character()
                user.add.character(new_character)
            if command == "2":
                pass
            if command == "3":
                pass


    def instructions(self):
        print("Lopeta: 0")
        print("Tee uusi hahmo: 1")
        print("Pelaa ja muokkaa tekemääsi hahmoa: 2")
        print("Tee uusi hahmoluokka: 3")


Interface()