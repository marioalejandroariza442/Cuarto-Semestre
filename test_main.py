# archivo: test_main.py
import unittest
import main

class TestMain(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(main.suma(5, 7), 12)
        self.assertEqual(main.suma(-1, 1), 0)

    def test_resta(self):
        self.assertEqual(main.resta(10, 3), 7)
        self.assertEqual(main.resta(0, 5), -5)

if __name__ == "__main__":
    unittest.main()
