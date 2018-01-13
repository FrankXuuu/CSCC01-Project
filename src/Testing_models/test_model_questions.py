import unittest
import sys

class TestModelQuestionTemplate(unittest.TestCase):

    def setUp(self):
        sys.path.insert(0, "../../src")
        from models import QuestionTemplate, TrueFalse, MultipleChoice, ShortAnswer
        self.short_question = QuestionTemplate(1, "What is the meaning of life?", "ShortAnswer", 1)
        self.tf_question = QuestionTemplate(2, "is a + b a number?", "TrueFalse", 1)
        self.mc_question = QuestionTemplate(1, "is it a b or c", "MultipleChoice", 2)

    def test_get_id(self):
        self.assertEqual(self.short_question.get_id(), 1, "Wrong id")
        self.assertEqual(self.tf_question.get_id(), 2, "Wrong id")
        self.assertEqual(self.mc_question.get_id(), 1, "Wrong id")

    def test_repr(self):
        self.assertEqual(self.short_question.__repr__(), "Question 1")
        self.assertEqual(self.tf_question.__repr__(), "Question 2")
        self.assertEqual(self.mc_question.__repr__(), "Question 1")

    def test_setup_question_text(self):
        self.assertEqual(self.short_question.question_text, "What is the meaning of life?")
        self.assertEqual(self.tf_question.question_text, "is a + b a number?")
        self.assertEqual(self.mc_question.question_text, "is it a b or c")

    def test_setup_question_type(self):
        self.assertEqual(self.short_question.question_type, "ShortAnswer")
        self.assertEqual(self.tf_question.question_type, "TrueFalse")
        self.assertEqual(self.mc_question.question_type, "MultipleChoice")

    def test_setup_assignment_id(self):
        self.assertEqual(self.short_question.assignment_id, 1)
        self.assertEqual(self.tf_question.assignment_id, 1)
        self.assertEqual(self.mc_question.assignment_id, 2)

if __name__ == '__main__':
    unittest.main()
