import unittest
from questions import QuestionTemplate

class TestQuestions(unittest.TestCase):
    
    def test_init_no_file(self):
        question_temp = QuestionTemplate(False, False, "___", "17")
        low = 1
        high = 99
        rand = question_temp.question_generator()
        between = 1 <= rand and 99 >= rand
        self.assertTrue(rand)
        self.assertEqual(question_temp.solution_generator(), 17)
        
    def test_question_generator(self):
        question_temp = QuestionTemplate(False, False, "h___v", "17")
        rand = question_temp.question_generator()
        result = rand[1] in ("1234567890")
        self.assertTrue(result)        
        
    def test_init_file(self):
        question_temp = QuestionTemplate('question-test', 'solution-test')
        rand = question_temp.question_generator()
        result = rand[9] in ("1234567890")
        self.assertTrue(rand)
        self.assertEqual(question_temp.solution_generator(), 1234321)
        
    def test_init_file_and_body(self):
        question_temp = QuestionTemplate('question-test', 'solution-test', "___", "17")
        rand = question_temp.question_generator()
        result = rand[9] in ("1234567890")
        self.assertTrue(rand)
        self.assertEqual(question_temp.solution_generator(), 1234321)    
    
    
if __name__ == '__main__':
    unittest.main(exit=False)