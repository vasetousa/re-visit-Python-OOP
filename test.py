# test suite
import unittest


class TestStringMethods(unittest.TestCase):

    # negative test function to test if values1 is less or equal than value2
    def test_negativeForLessEqual(self):
        first = 5
        second = 6

        # error message in case if test case got failed
        message = "first value is not less than or equal to second value."

        # assert function() to check if values1 is less or equal than value2
        self.assertLessEqual(first, second, message)


if __name__ == '__main__':
    unittest.main()
