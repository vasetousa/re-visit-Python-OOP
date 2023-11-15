from unittest import TestCase as Test, main
from Testing.CarManager.car_manager import Car


class TestCar(Test):
    def setUp(self):
        self.car = Car("Mercedes", 'E350', 6, 80)
        self.current_fuel = self.car.fuel_amount

    def test_proper_init(self):
        self.assertEqual(self.car.make, "Mercedes")
        self.assertEqual(self.car.model, "E350")
        self.assertEqual(self.car.fuel_consumption, 6)
        self.assertEqual(self.car.fuel_capacity, 80)
        self.assertEqual(self.car.fuel_amount, 0)

    def test_car_make_setter__if_null_raises(self):
        # tests for null make
        with self.assertRaises(Exception) as ex:
            self.car.make = ''
        self.assertEqual(str(ex.exception), "Make cannot be null or empty!")
        # tests for proper name change
        self.assertEqual(self.car.make, 'Mercedes')
        new_make = 'Mercedes Sport'
        self.car.make = new_make
        self.assertEqual(self.car.make, new_make)

    def test_car_model_setter__if_null_raises(self):
        # tests for null model
        with self.assertRaises(Exception) as ex:
            self.car.model = ''
        self.assertEqual(str(ex.exception), "Model cannot be null or empty!")
        # tests for proper name change
        self.assertEqual(self.car.model, 'E350')
        new_model = 'E350SS diesel'
        self.car.model = new_model
        self.assertEqual(self.car.model, new_model)

    def test_fuel_consumption_setter__if_zero_or_negative_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0
        self.assertEqual(str(ex.exception), "Fuel consumption cannot be zero or negative!")
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = - 1
        self.assertEqual(str(ex.exception), "Fuel consumption cannot be zero or negative!")
        # setting new value
        nfc = 12
        self.car.fuel_consumption = nfc
        self.assertEqual(self.car.fuel_consumption, nfc)

    def test_fuel_capacity_setter__if_zero_or_negative_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0
        self.assertEqual(str(ex.exception), "Fuel capacity cannot be zero or negative!")
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = - 1
        self.assertEqual(str(ex.exception), "Fuel capacity cannot be zero or negative!")
        # setting new value
        nfc = 100
        self.car.fuel_capacity = nfc
        self.assertEqual(self.car.fuel_capacity, nfc)

    def test_fuel_amount_setter__if_zero_or_negative_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = - 1
        self.assertEqual(str(ex.exception), "Fuel amount cannot be negative!")
        # setting new value
        nfc = 100
        self.car.fuel_amount = nfc
        self.assertEqual(self.car.fuel_amount, nfc)

    def test_refuel_setter__if_zero_or_negative_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)
        self.assertEqual(str(ex.exception), "Fuel amount cannot be zero or negative!")
        with self.assertRaises(Exception) as ex:
            self.car.refuel(-1)
        self.assertEqual(str(ex.exception), "Fuel amount cannot be zero or negative!")

    def test_refuel_adds_fuel(self):
        # test if fuel was added to the fuel_amount
        self.assertEqual(self.car.fuel_amount, 0)
        new_fuel_amount_to_add = 100
        self.car.refuel(new_fuel_amount_to_add)
        self.assertGreater(self.car.fuel_amount, 0)

    def test_setting_proper_capacity(self):
        # test if fuel_amount was set properly
        self.assertEqual(self.car.fuel_amount, 0)
        self.car.refuel(100)
        self.assertEqual(self.car.fuel_capacity, 80)

    def test_proper_refuel(self):
        self.assertEqual(self.car.fuel_amount, 0)
        self.car.refuel(10)
        self.assertEqual(self.car.fuel_amount, 10)

    def test_drive__if_not_enough_fuel_raises(self):
        # testing with small amount of fuel
        self.car.fuel_amount = 10
        with self.assertRaises(Exception) as ex:
            self.car.drive(500)
        self.assertEqual(str(ex.exception), "You don't have enough fuel to drive!")

    def test_drive_with_enough_fuel_sets_proper_fuel_amount(self):
        self.car.fuel_amount = 40
        self.car.drive(500)
        self.assertNotEqual(self.car.fuel_amount, 40)


if __name__ == '__main__':
    main()