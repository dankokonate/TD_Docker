import unittest
from Personne import Personne
from Ssn import Ssn


class test_person(unittest.TestCase):
    def test_personne(self):
        ssn = Ssn("269054958815780")
        personne = Personne("Toto", "Tata", ssn)
        self.assertEqual(personne.hasValid(), True)


if __name__ == "__main__":
    unittest.main()
