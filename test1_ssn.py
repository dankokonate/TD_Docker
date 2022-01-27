import unittest
from Ssn import Ssn

class test1_snn(unittest.TestCase):
    def test1_snn(self):
        ssn = Ssn("269054958815780")
        self.assertEqual(ssn.is_valid(), True)


if __name__ == "__main__":
    unittest.main()
