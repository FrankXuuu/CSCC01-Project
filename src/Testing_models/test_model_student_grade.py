import unittest
import sys

class TestModelStudentGrade(unittest.TestCase):

    def setUp(self):
        sys.path.insert(0, "../../src")
        from models import StudentGrade
        self.grade1 = StudentGrade(1, 2)
        self.grade2 = StudentGrade(3, 4)
        
    def test_setup_student_id(self):
        self.assertEqual(self.grade1.student_id, 1)
        self.assertEqual(self.grade2.student_id, 3)

    def test_setup_assignment_id(self):
        self.assertEqual(self.grade1.assignment_id, 2)
        self.assertEqual(self.grade2.assignment_id, 4)


if __name__ == '__main__':
    unittest.main()
