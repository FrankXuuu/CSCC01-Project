import unittest
import datetime
import sys

class TestModelAssignment(unittest.TestCase):

    def setUp(self):
        sys.path.insert(0, "../../src")
        from models import Assignment
        start_date = datetime.date(2000, 5, 5)
        due_date = datetime.date(2020, 12, 12)
        self.assignment1 = Assignment(1)
        self.assignment2 = Assignment(2, start_date, due_date)
    
    def test_assignment_start_date(self):
        answer1 = datetime.date(2000, 1, 1)
        answer2 = datetime.date(2000, 5, 5)
        self.assertEqual(self.assignment1.start_date, answer1)
        self.assertEqual(self.assignment2.start_date, answer2)

    def test_assignment_due_date(self):
        due_date1 = datetime.date(2000, 1, 1)
        due_date2 = datetime.date(2020, 12, 12)
        self.assertEqual(self.assignment1.end_date, due_date1)
        self.assertEqual(self.assignment2.end_date, due_date2)

    def test_assignment_id(self):
        self.assertEqual(self.assignment1.assignment_id, 1)
        self.assertEqual(self.assignment2.assignment_id, 2)

    def test_assignment_repr(self):
        self.assertEqual(self.assignment1.__repr__(), "Assignment 1")
        self.assertEqual(self.assignment2.__repr__(), "Assignment 2")

if __name__ == '__main__':
    unittest.main()
