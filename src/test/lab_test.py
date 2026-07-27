import unittest

from src.main.lab import problem1


class LabTest(unittest.TestCase):
    def test_activity_inner_join1(self):
        expected = {
            (2, "Stephen Colbert"),
            (3, "Samantha Bee"),
            (5, "Robert Riggle"),
        }

        result = problem1()

        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
