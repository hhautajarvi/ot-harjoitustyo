class Character:
    def __init__(self, name: str):
        self.name = name
        self.dwclass = None
        self.alignment = None
        self.race = None
        self.image = None
        self.stats = {"strength": None, "dexterity": None, "constitution": None,
                      "intelligence": None, "wisdom": None, "charisma": None}
        self.backstory = None
        self.looks = None

    def choose_class(self, dw_class):
        self.dwclass = dw_class

    def choose_alignment(self, alignment: int):
        self.alignment = alignment

    def choose_race(self, race: int):
        self.race = race

    def choose_stats(self, statlist: list):
        self.stats["strength"] = statlist[0]
        self.stats["dexterity"] = statlist[1]
        self.stats["constitution"] = statlist[2]
        self.stats["intelligence"] = statlist[3]
        self.stats["wisdom"] = statlist[4]
        self.stats["charisma"] = statlist[5]

    def load_stats(self, stats: dict):
        self.stats = stats

    def choose_backstory(self, story: str):
        self.backstory = story

    def choose_looks(self, looks: str):
        self.looks = looks

    def choose_image(self, image_address):
        self.image = image_address
