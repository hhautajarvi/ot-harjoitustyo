import unittest
from characters import Character


class TestCharacter(unittest.TestCase):
    def setUp(self):
        self.char = Character("testname")

    def test_constructor_name_correct(self):
        self.assertEqual(self.char.name, "testname")

    def test_choose_class(self):
        self.char.choose_class(1)
        self.assertEqual(self.char.dwclass, 1)

    def test_choose_alignment(self):
        self.char.choose_alignment(2)
        self.assertEqual(self.char.alignment, 2)

    def test_choose_race(self):
        self.char.choose_race(3)
        self.assertEqual(self.char.race, 3)

    def test_choose_stats(self):
        self.char.choose_stats([16, 15, 13, 12, 9, 8])
        self.assertEqual(self.char.stats["strength"], 16)
        self.assertEqual(self.char.stats["dexterity"], 15)
        self.assertEqual(self.char.stats["constitution"], 13)
        self.assertEqual(self.char.stats["intelligence"], 12)
        self.assertEqual(self.char.stats["wisdom"], 9)
        self.assertEqual(self.char.stats["charisma"], 8)

    def test_load_stats(self):
        stats = {"strength": 16, "dexterity": 15, "constitution": 13,
                 "intelligence": 12, "wisdom": 9, "charisma": 8}
        self.char.load_stats(stats)
        self.assertEqual(self.char.stats["strength"], 16)
        self.assertEqual(self.char.stats["dexterity"], 15)
        self.assertEqual(self.char.stats["constitution"], 13)
        self.assertEqual(self.char.stats["intelligence"], 12)
        self.assertEqual(self.char.stats["wisdom"], 9)
        self.assertEqual(self.char.stats["charisma"], 8)

    def test_choose_backstory(self):
        self.char.choose_backstory("Hahmo syntyi ja eli")
        self.assertEqual(self.char.backstory, "Hahmo syntyi ja eli")

    def test_choose_looks(self):
        self.char.choose_looks("Hahmo on komea")
        self.assertEqual(self.char.looks, "Hahmo on komea")

    def test_choose_image(self):
        self.char.choose_image("src/kuva.jpg")
        self.assertEqual(self.char.image, "src/kuva.jpg")
