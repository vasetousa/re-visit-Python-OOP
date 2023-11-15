from unittest import TestCase as Case, main
from Testing.List.extended_list import IntegerList


# testing the methods was done using the method get_data() (line 17)
# w/o this method we can use self.il._IntegerList__data, because __data is a private attribute
# (example line 18) !!!

class TestList(Case):

    def setUp(self):
        self.data_list = [1, 2, 'Peter']
        self.il = IntegerList(*self.data_list)
        self.index_len = len(self.il.get_data())

    def test_if_proper_init(self):
        self.assertEqual(self.il.get_data(), [1, 2])
        # self.assertEqual(self.il._IntegerList__data, [1, 2])

    def test_add_element_to_list_if_not_int_raises(self):
        # part 1
        with self.assertRaises(ValueError) as ve:
            self.il.add('Peter')
        self.assertEqual(str(ve.exception), 'Element is not Integer')
        # part 2
        self.assertNotEqual(self.il.get_data(), [1, 2, 100])
        self.il.add(100)
        self.assertEqual(self.il.get_data(), [1, 2, 100])

    def test_remove_index_from_list_if_out_of_range_raises(self):
        # part 1
        self.assertNotEqual(self.index_len, 3)
        with self.assertRaises(IndexError) as ie:
            self.il.remove_index(3)
        self.assertEqual(str(ie.exception), 'Index is out of range')
        # part 2
        self.assertEqual(self.il.get_data(), [1, 2])
        self.il.remove_index(1)
        self.assertEqual(self.il.get_data(), [1])

    def test_get_element_from_index_if_index_out_of_range_raises(self):
        # part 1
        self.assertNotEqual(self.index_len, 3)
        with self.assertRaises(IndexError) as ie:
            self.il.get(3)
        self.assertEqual(str(ie.exception), 'Index is out of range')
        # part 2
        self.assertEqual(self.il.get_data(), [1, 2])
        el = self.il.get(1)
        self.assertEqual(el, 2)

    def test_insert_raises(self):
        # part 1 if element is not integer
        with self.assertRaises(ValueError) as ve:
            self.il.insert(0, 'Peter')
        self.assertEqual(str(ve.exception), 'Element is not Integer')
        # part 2 if index is out of range
        self.assertNotEqual(self.index_len, 3)
        with self.assertRaises(IndexError) as ie:
            self.il.insert(3, 100)
        self.assertEqual(str(ie.exception), 'Index is out of range')
        # part 3 if element was insert in the list
        self.assertEqual(self.il.get_data(), [1, 2])
        self.il.insert(1, 100)
        self.assertEqual(self.il.get_data(), [1, 100, 2])

    def test_get_biggest_element(self):
        self.il.insert(1, 100)
        self.assertEqual(self.il.get_data(), [1, 100, 2])

        self.assertEqual(self.il.get_biggest(), 100)

    def test_get_index(self):
        self.assertEqual(self.il.get_data(), [1, 2])
        # check if element (1) is at index (0)
        self.assertEqual(self.il.get_index(1), 0)
        self.assertEqual(self.il.get_index(2), 1)


if __name__ == '__main__':
    main()
