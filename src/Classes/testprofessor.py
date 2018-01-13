import unittest
from professor import Professor

class TestProfessor(unittest.TestCase):
    
    
    def setUp(self):
        self.profA = Professor()
        self.profB = Professor("Frank Xu")
        
    def test_str(self):
        self.assertEqual(str(self.profA), "Name: Sohee Kang;", "incorrect initialization")        
        
    def test_compare_str(self):
        self.assertNotEqual(str(self.profA), str(self.profB), "incorrect string generation")
    
    
if __name__ == '__main__':
    unittest.main(exit=False)
    