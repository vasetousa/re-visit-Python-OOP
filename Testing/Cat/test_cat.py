from unittest import TestCase as Case, main
from .cat import Cat


class CatTests(Case):
    def setUp(self):
        self.cat = Cat('Masha')

    def test_if_init(self):
        self.assertEqual(self.cat.name, 'Masha')

    def test_cat_size_increase_after_eating(self):
        self.assertFalse(self.cat.fed)
        self.cat.eat()
        self.assertEqual(self.cat.size, 1)

    def test_cat_fed_after_eating(self):
        self.assertFalse(self.cat.fed)
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_cat_cant_eat_if_fed_raises_error(self):
        self.cat.fed = True
        with self.assertRaises(Exception) as ex:
            self.cat.eat()
        self.assertEqual(str(ex.exception), 'Already fed.')

    def test_cat_cant_sleep_if_not_fed_raises_error(self):
        self.assertFalse(self.cat.fed)
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()
        self.assertEqual(str(ex.exception), 'Cannot sleep while hungry')

    def test_cat_not_sleepy_after_sleep(self):
        self.assertFalse(self.cat.fed)
        self.cat.eat()
        self.assertTrue(self.cat.sleepy)
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    main()
