import unittest
from Testing.Exercises.hero.project.hero import Hero


class TestHero(unittest.TestCase):
    def setUp(self):
        self.hero = Hero('Tron', 10, 200, 100)
        self.strong_hero = Hero('Tron', 11, 1000000, 1000)
        self.enemy_hero = Hero('Hulk', 10, 300, 150)
        self.strong_enemy_hero = Hero('Hulk', 11, 200000, 1500)

    def test_proper_init(self):
        self.assertEqual(self.hero.username, 'Tron')
        self.assertEqual(self.hero.level, 10)
        self.assertEqual(self.hero.health, 200)
        self.assertEqual(self.hero.damage, 100)

    def test_if_self_name_provided_for_battle__raises(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        self.assertEqual(str(ex.exception), "You cannot fight yourself")

    def test_if_hero_hp_is_zero__raises(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy_hero)
        self.assertEqual(str(ve.exception), "Your health is lower than or equal to 0. You need to rest")

    def test_if_enemy_hero_hp_is_zero__raises(self):
        self.enemy_hero.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy_hero)
        self.assertEqual(str(ve.exception), f"You cannot fight {self.enemy_hero.username}. He needs to rest")

    def test_after_battle_if_hero_hp_decreases(self):
        self.assertEqual(self.hero.health, 200)
        self.hero.battle(self.enemy_hero)
        self.assertEqual(self.hero.health, -1300)

    def test_after_battle_if_enemy_hero_hp_decreases(self):
        self.assertEqual(self.enemy_hero.health, 300)
        self.hero.battle(self.enemy_hero)
        self.assertEqual(self.enemy_hero.health, -700)

    def test_battle_draw(self):
        result = self.hero.battle(self.enemy_hero)
        self.assertEqual(result, 'Draw')

    def test_you_win(self):
        result = self.strong_hero.battle(self.enemy_hero)
        self.assertEqual(result, 'You win')
        self.assertEqual(self.strong_hero.level, 12)
        self.assertEqual(self.strong_hero.health, 998505)
        self.assertEqual(self.strong_hero.damage, 1005)

    def test_you_lose(self):
        result = self.hero.battle(self.strong_enemy_hero)
        self.assertEqual(result, 'You lose')
        self.assertEqual(self.strong_enemy_hero.level, 12)
        self.assertEqual(self.strong_enemy_hero.health, 199005)
        self.assertEqual(self.strong_enemy_hero.damage, 1505)

    def test_str(self):
        self.assertEqual(str(self.hero), "Hero Tron: 10 lvl\nHealth: 200\nDamage: 100\n")


if __name__ == '__main__':
    unittest.main()
