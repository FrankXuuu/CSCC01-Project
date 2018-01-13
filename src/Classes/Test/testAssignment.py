import unittest
from assignment import Assignment


class TestAssignment(unittest.TestCase):

    def test_get_ID(self):
        assignment_test = Assignment(1)
        self.assertEqual(assignment_test.assignment_ID(), 1)

    def test_set_ID(self):
        assignment_test = Assignment(1, (2020, 1, 1), (2050, 1, 1), 0)
        assignment_test.assignment_ID(2)
        self.assertEqual(assignment_test.assignment_ID(), 2)

    def test_assignment_start_date(self):
        assignment = Assignment(0)
        self.assertEqual(assignment.assignment_start_date(), (2000, 1, 1))

    def test_assignment_due_date(self):
        assignment = Assignment(0)
        self.assertEqual(assignment.assignment_due_date(), (2000, 1, 1))

    def test_assignment_due_date_set(self):
        assignment = Assignment(0)
        assignment.assignment_due_date((2020, 1, 1))
        self.assertEqual(assignment.assignment_due_date(), (2020, 1, 1))
        
if __name__ == '__main__':
    unittest.main()
