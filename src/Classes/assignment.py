"""
Assignment Class

"""

from questions import *
from datetime import date

import sys
import json


class Assignment(object):
    """The Assignment that is designed by the professor, done by the student.

    Attributes:
     qt_file: A JSON file where all the question templates for this assignment
                are stored.
     sol_file: A JSON file where all the solution formulas for this assignment
     are stored.
     __id: The id of this assignment
     __start_date: The time when this assignment becomes available for
                students. Format: YYYYMMDD
     __due_date: The time when this assignment becomes unavailable for students
                 to edit. Format: YYYYMMDD
     __grade: The final grade of this assignment.
     __question_templates: A list containing all the QuestionTemplates


    """

    def __init__(self, id, start_date=date(2000, 1, 1),
                 due_date=date(2000, 1, 1), grade=0):
        """Initializes an inst an ce of assignment
    """
        self.__id = id
        self.__start_date = start_date
        self.__due_date = due_date
        self.__grade = 0
        self.__question_templates = []
        self.qt_file = open("assignments/"+str(self.__id)+"assignment_qt.json",
                            'a')
        self.sol_file = open("assignmentsSol/"+str(self.__id)+"assignment_sol.json", 'a')

    @property
    def assignment_ID(self):
        """Getter for __id
        Returns:
         self.__id
        """

        return self.__id

    @assignment_ID.setter
    def assignment_ID(self, new_ID):
        """Setter for __ID. Updates the ID of this assignment to its new value.
    Parameters:
    new_ID: The new desired value for the ID
"""
        self.__id = new_ID

    # Getter and setter for start_date

    @property
    def assignment_start_date(self):
        """Getter for __start_date
    Returns:
     self.__start_date: Start date for this assignment

"""

        return self.__start_date

    @assignment_start_date.setter
    def assignment_start_date(self, new_start_date):
        """Setter for __start_date. Updates the start date of this assignment
        to its new value.
    Parameters:
    new_start_date: The new desired value for the start date
"""
        self.__start_date = new_start_date

    # Getter and setter for due_date

    @property
    def assignment_due_date(self):
        """Getter for __due_date
    Returns:
     self.__due_date: Due date for this assignment

"""

        return self.__due_date

    @assignment_due_date.setter
    def assignment_due_date(self, new_due_date):
        """
        Setter for __due_date. Updates the due date of this
        assignment to its new value.
        Parameters:
            new_due_date: The new desired value for the due date
        """
        self.__due_date = new_due_date

    def grade_assignment(self):
        """Grades the assignmnet"""
        grade = 0
        grades_file = open("grades/"+str(self.__id)+"grades", 'a')
        self.sol_file = open("assignmentsSol/"+str(self.__id)+"assignment_sol.json", 'r')
        student_sol_file = open("studentSol/"+str(self.__id)+"assignment_sol.json", 'r')
        for line in student_sol_file:
            if json.loads(line) == json.loads(self.sol_file.readline()):
                grade += 1
        grades_file.write(json.dumps(grade)+'\n')
        return grade

    def build_assignment(self):
        """Prof: Builds an assignment containing multiple QuestionTemplates and
        saves them in a JSON file."""
        exit_condition = None
        while exit_condition != "EX":

            address = input("Please enter the address of the templateFile")
            solution_address = input("Please enter the address of the solution"
                                     )

            self.__question_templates.append(QuestionTemplate(address,
                                                              solution_address)
                                             )
            exit_condition = input(
                "If you're done with the assignment, please enter "
                "EX. If not, press Enter.")

        for qt in self.__question_templates:
            self.qt_file.write(json.dumps(qt, cls=QtEncoder) + '\n')
            self.sol_file.write(json.dumps(qt.solution_generator())+'\n')

    def generate_assignment(self):
        """Student: Creates an instance of assignment where the QuestionTemplate values
        are random. Saves the instance in a JSON file."""
        assignment_instance = open("assignmentInstances/"+str(self.__id)+"assignment_instance.json", 'w')
        assignment_instance_solution = open("assignmentInstancesSol/"+str(self.__id)+"assignment_instance_sol.json", 'w')
        self.qt_file = open("assignments/"+str(self.__id)+"assignment_qt.json", 'r')
        self.sol_file = open("assignmentsSol/"+str(self.__id)+"assignment_sol.json", 'r')
        for line in self.qt_file:
            qt = QuestionTemplate(body=json.loads(line), solution=json.loads(self.sol_file.readline()))
            assignment_instance.write(
                json.dumps(qt.question_generator()) + '\n')
            assignment_instance_solution.write(json.dumps(qt.solution_generator()) + '\n')

    def complete_assignment(self):
        grades_file = open("grades/"+str(self.__id)+"grades", 'r')
        grades = grades_file.read().split()
        grades.sort()
        grades_file = open("grades/"+str(self.__id)+"grades", 'w')
        grades_file.write(json.dumps(grades.pop()))

    def save_assignment(self):
        return None
