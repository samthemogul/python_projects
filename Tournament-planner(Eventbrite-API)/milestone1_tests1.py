import unittest
from datetime import datetime
from untested_helpers import from_datetime_to_string, power_of_two, compute_round_name

class TestHelpers(unittest.TestCase):

    def from_datetime_to_string_test(self):
        datetime_object = datetime(2023, 12, 15, 12, 0, 0)
        result = from_datetime_to_string(datetime_object)
        self.assertEqual(result, "2023-01-01T12:00:00Z")

    def power_of_two_test(self):
        self.assertTrue(power_of_two(8))
        self.assertFalse(power_of_two(5))
        self.assertFalse(power_of_two(14))

    def compute_round_name_test(self):
        self.assertEqual(compute_round_name(1), 'Final')
        self.assertEqual(compute_round_name(2), 'Semi-Finals')
        self.assertEqual(compute_round_name(4), 'Quarter-Finals')
        self.assertEqual(compute_round_name(8), 'Round of 16')

    def compute_round_name_with_string_test(self):
        self.assertEqual(compute_round_name("4"), 'Quarter-Finals')

    def compute_round_name_invalid_input_test(self):
        with self.assertRaises(TypeError):
            compute_round_name("one")

if __name__ == '__main__':
    unittest.main()
