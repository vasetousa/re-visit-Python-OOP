import unittest

from project.truck_driver import TruckDriver


class TestTruckDriver(unittest.TestCase):
    def setUp(self):
        self.driver = TruckDriver('Ivan', 1.50)

    def test_if_proper_init(self):
        self.assertEqual(self.driver.name, 'Ivan')
        self.assertEqual(self.driver.money_per_mile, 1.50)
        self.assertEqual(self.driver.earned_money, 0)
        self.assertEqual(self.driver.miles, 0)
        self.assertEqual(self.driver.available_cargos, {})

    def test_driver_bankrupt(self):
        self.driver.money_per_mile = 0.02
        self.driver.add_cargo_offer("Paris", 2000)

        with self.assertRaises(ValueError) as ve:
            self.driver.drive_best_cargo_offer()
        self.assertEqual(str(ve.exception), f"{self.driver.name} went bankrupt.")

    def test_add_cargo_offer__if_cargo_already_added(self):
        self.driver.available_cargos = {'Sofia': 500}
        with self.assertRaises(Exception) as ex:
            self.driver.add_cargo_offer('Sofia', 500)
        self.assertEqual(str(ex.exception), "Cargo offer is already added.")

    def test_add_cargo_offer__adds_cargo(self):
        self.driver.add_cargo_offer('Sofia', 500)
        self.assertEqual(self.driver.available_cargos, {'Sofia': 500})

    def test_add_cargo_offer_message(self):
        self.assertEqual(self.driver.add_cargo_offer('Sofia', 500), f"Cargo for 500 to Sofia was added as an offer.")

    def test_drive_best_cargo_offer_message(self):
        self.assertEqual(self.driver.available_cargos, {})
        self.assertEqual(self.driver.drive_best_cargo_offer(), "There are no offers available.")

    def test_drive_best_cargo_offer(self):
        self.driver.add_cargo_offer('Sofia', 500)
        self.driver.add_cargo_offer('Varna', 1000)
        result = self.driver.drive_best_cargo_offer()
        self.assertEqual(result, f"{self.driver.name} is driving 1000 to Varna.")
        self.assertEqual(self.driver.earned_money, 1375)
        self.assertEqual(self.driver.miles, 1000)

    def test_eat(self):
        self.driver.earned_money = 200
        self.driver.eat(250)
        self.driver.eat(500)

        self.assertEqual(self.driver.earned_money, 160)

    def test_sleep(self):
        self.driver.earned_money = 200
        self.driver.sleep(1000)
        self.driver.sleep(2000)

        self.assertEqual(self.driver.earned_money, 110)

    def test_pump_gas(self):
        self.driver.earned_money = 3000
        self.driver.pump_gas(1500)
        self.driver.pump_gas(3000)

        self.assertEqual(self.driver.earned_money, 2000)

    def test_repair_truck(self):
        self.driver.earned_money = 30000
        self.driver.repair_truck(10000)
        self.driver.repair_truck(20000)

        self.assertEqual(self.driver.earned_money, 15000)

    def test_repr(self):
        self.assertEqual(str(self.driver), f'Ivan has 0 miles behind his back.')


if __name__ == '__main__':
    unittest.main()
