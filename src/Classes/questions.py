import random
import json


class QtEncoder(json.JSONEncoder):
    """JSON Encoder for QuestionTemplate Class"""
    def default(self, obj):
        if isinstance(obj, QuestionTemplate):
            return obj.body
        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)


class QuestionTemplate():
    """Question Template which contains a body of text, and variables.

    Attributes:
     data: List of all the variables
     template_file: The JSON file on which this QuestionTemplate is stored.
     template_solution: The JSON file on which the formula is stored.
     body: The body of text for this QuestionTemplate

    """
    def __init__(self, template_file=None, solution_file=None, body=None,
                 solution=None):
        """Initializes a QuestionTemplate object."""
        self.data = []
        if template_file:
            self.template_file = open(template_file, "r")
            self.template_solution = open(solution_file, "r")
            self.body = self.template_file.read()
            self.solution = self.template_solution.read()
        else:
            self.body = body
            self.solution = solution

    def question_generator(self):
        """
    Returns a string where the variables are replaced with random values
    """
        q = self.body[:]
        while(q.find("___") != -1):
            self.data.append(random.randint(1, 100))
            q = q.replace("___", str(self.data[(len(self.data)-1)]), 1)
        return q

    def solution_generator(self):
        return int(self.solution)

    def grade_question():
        return None
