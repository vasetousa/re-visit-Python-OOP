import unittest
from project.trip import Trip


class TripTest(unittest.TestCase):
    def setUp(self):
        self.trip = Trip(10000, 1, False)
        self.family_trip = Trip(50000, 2, True)

    def test_proper_init(self):
        self.assertEqual(self.trip.budget, 10000)
        self.assertEqual(self.trip.travelers, 1)
        self.assertEqual(self.trip.is_family, False)
        self.assertEqual(self.trip.booked_destinations_paid_amounts, {})

    def test_less_than_1_traveler_(self):
        with self.assertRaises(ValueError) as ve:
            self.trip.travelers = 0
        self.assertEqual(str(ve.exception), 'At least one traveler is required!')

    def test_is_family_(self):
        self.trip.travelers = 1
        self.trip.is_family = True
        self.assertEqual(self.trip.is_family, False)

        self.trip.travelers = 2
        self.trip.is_family = True
        self.assertEqual(self.trip.is_family, True)

    def test_book_a_trip_no_destination_(self):
        self.DESTINATION_PRICES_PER_PERSON = {}
        self.assertEqual(self.trip.book_a_trip('USA'), 'This destination is not in our offers, '
                                                       'please choose a new one!')

    def test_book_a_trip_with_destination_no_family(self):
        self.trip.book_a_trip('Bulgaria')
        self.assertEqual(self.trip.booked_destinations_paid_amounts, {'Bulgaria': 500})
        self.assertEqual(self.trip.budget, 9500)

    def test_book_a_trip_with_destination_with_family(self):
        self.family_trip.book_a_trip('New Zealand')
        self.assertEqual(self.family_trip.booked_destinations_paid_amounts, {'New Zealand': 13500.0})
        self.assertEqual(self.family_trip.budget, 36500.0)

    def test_book_a_trip_with_destination_message_(self):
        # message success
        result = self.family_trip.book_a_trip('New Zealand')
        self.assertEqual(result, 'Successfully booked destination New Zealand! Your budget left is 36500.00')

    def test_book_a_trip_with_destination_low_budget(self):
        self.low_budget_trip = Trip(100, 1, False)
        result = self.low_budget_trip.book_a_trip('New Zealand')
        self.assertEqual(result, 'Your budget is not enough!')

    def test_booking_status_no_bookings(self):
        result = self.trip.booking_status()
        self.assertEqual(result, f'No bookings yet. Budget: 10000.00')

    def test_booking_status_with_bookings(self):
        self.trip.book_a_trip('New Zealand')

        self.assertEqual(self.trip.booking_status(), "Booked Destination: New Zealand\n"
                                                     "Paid Amount: 7500.00\n"
                                                     "Number of Travelers: 1\n"
                                                     "Budget Left: 2500.00")
