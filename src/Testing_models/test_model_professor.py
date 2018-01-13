import unittest
import sys

class TestModelProfessor(unittest.TestCase):

    def setUp(self):
        sys.path.insert(0, "../../src")
        from models import Professor
        self.sohee = Professor("sohee@utsc.ca", "sohee2017")
        self.bob = Professor("Bobby@kys.ca", "please", "Bob the Builder")

    def test_setup_name(self):
        self.assertEqual(self.sohee.name, "Sohee Kang", "Name not set correctly")
        self.assertEqual(self.bob.name, "Bob the Builder", "Name not set")

    def test_email(self):
        self.assertEqual(self.sohee.email, "sohee@utsc.ca", "Email not set")

    def test_password(self):
        self.assertEqual(self.bob.password, "please", "Incorrect password")


if __name__ == '__main__':
    unittest.main()
