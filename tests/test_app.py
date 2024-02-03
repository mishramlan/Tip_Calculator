import unittest
from tip_calculator import calculate_tip

class TestTipCalculator(unittest.TestCase):
    def test_calculate_tip(self):
        self.assertAlmostEqual(calculate_tip(100, 15), 15.0)
        self.assertAlmostEqual(calculate_tip(50, 20), 10.0)
        self.assertAlmostEqual(calculate_tip(75.5, 18), 13.59)

if __name__ == "__main__":
    unittest.main()