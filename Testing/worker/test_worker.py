import unittest
from .worker import Worker


class WorkerTests(unittest.TestCase):

    def setUp(self):
        self.worker = Worker('Ivan', 1500, 100)

    def test_init_worker(self):
        self.assertEqual(self.worker.name, "Ivan")
        self.assertEqual(self.worker.salary, 1500)
        self.assertEqual(self.worker.energy, 100)
        self.assertEqual(self.worker.money, 0)

    def test_energy_incremented_after_call_rest(self):
        self.worker.rest()
        self.assertEqual(self.worker.energy, 101)

    def test_if_worker_works_with_negative_energy_or_0_raise(self):
        self.worker.energy = 0
        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_if_money_is_increased_after_work_called(self):
        self.worker.work()
        self.assertEqual(self.worker.money, 1500)

    def test_if_energy_is_decreased_after_work_called(self):
        self.worker.work()
        self.assertEqual(self.worker.energy, 99)

    def test_if_correct_string_return_after_info_reqiested(self):
        string = self.worker.get_info()
        self.assertEqual(string, 'Ivan has saved 0 money.')


if __name__ == '__main__':
    unittest.main()
