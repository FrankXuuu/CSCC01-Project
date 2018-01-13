import unittest
from student import Student


class TestStudent(unittest.TestCase):

    def testGetName(self):
        student = Student()
        self.assertEqual(student.getName(), "Jane Doe")

    def testGetStudentID(self):
        student = Student()
        self.assertEqual(student.getStudentID(), "0")

    def testGetFinalGrade(self):
        student = Student()
        self.assertEqual(student.getFinalGrade(), 0)

    def testGetAssignmentGrades(self):
        student = Student()
        expected = []
        self.assertEqual(student.getAssignmentGrades(), expected)

    def testStudentGeorgie(self):
        student = Student("Georgie@email.com", "12334455", "Georgie", "Georgie", "1")
        self.assertEqual(student.getName(), "Georgie Georgie")
        self.assertEqual(student.getStudentID(), "1")
        self.assertEqual(student.getFinalGrade(), 0)
        expected = []
        self.assertEqual(student.getAssignmentGrades(), expected)

    def testHighestID(self):
        student = Student("email", "f", "Jz", "f", "2147483648")
        self.assertEqual(student.getStudentID(), "2147483648")

    def testNegativeID(self):
        student = Student("email", "f", "Jz", "f", "-2")
        self.assertEqual(student.getStudentID(), "-2")

    def testSymbolName(self):
        student = Student("email", "f", "*~!@`:''", "1213,.%'''")
        self.assertEqual(student.getName(), "*~!@`:'' 1213,.%'''")

    
if __name__ == '__main__':
    unittest.main()
