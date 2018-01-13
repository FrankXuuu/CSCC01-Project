import unittest
import sys

class TestModelStudent(unittest.TestCase):

    def setUp(self):
        sys.path.insert(0, "../../src")
        from models import Student
        self.genghis = Student(1, "Genghis", "Khan", "Genghis.Khan@utsc.ca", "Shinai")
        self.dropping = Student(2, "Dropping", "Soon", "cya@utsc.ca", "Goodby3")
    
    def test_setup_student_id(self):
        self.assertEqual(self.genghis.student_id, 1, "wrong ID")
        self.assertEqual(self.dropping.student_id, 2, "wrong ID")

    def test_setup_name(self):
        self.assertEqual(self.genghis.first_name, "Genghis", "Wrong first name")
        self.assertEqual(self.genghis.last_name, "Khan", "Wrong last name")
        self.assertEqual(self.dropping.first_name, "Dropping", "Wrong first name")
        self.assertEqual(self.dropping.last_name, "Soon", "Wrong last name")

    def test_setup_email(self):
        self.assertEqual(self.genghis.email, "Genghis.Khan@utsc.ca", "Wrong email")
        self.assertEqual(self.dropping.email, "cya@utsc.ca", "Wrong email")

    def test_setup_password(self):
        self.assertEqual(self.genghis.password, "Shinai", "Wrong password")
        self.assertEqual(self.dropping.password, "Goodby3", "Wrong password")


if __name__ == '__main__':
    unittest.main()
