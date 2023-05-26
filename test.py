import unittest
import xmlrunner
from Dodatak_A import OperationsManager
import math


class TestDivision(unittest.TestCase):
    def test_regular(self):
        om = OperationsManager(10, 5)
        result = om.perform_division()
        self.assertEqual(result, 2.0)

    def test_zero(self):
        om = OperationsManager(10, 0)
        result = om.perform_division()
        self.assertTrue(math.isnan(result))


if __name__ == "__main__":
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output="test-reports"))
