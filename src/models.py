from app import db
from sqlalchemy.dialects.postgresql import JSON
import parser
from random import randint
from re import findall

from datetime import date
import datetime

import json

class Professor(db.Model):
    """Professor class
Attributes:
Name: The name of the professor.

"""
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String())
    name = db.Column(db.String())
    password = db.Column(db.String(), nullable=False)

    def __init__(self, email, password, name="Sohee Kang"):
        """Initializes the Professor class"""
        self.email = email
        self.password = password
        self.name = name

class StudentGrade(db.Model):
    __tablename__ = 'student_grade'

    student_id = db.Column(db.Integer, db.ForeignKey('student.student_id'), primary_key=True)
    assignment_id = db.Column(db.Integer, primary_key=True) 
    grade = db.Column(db.Integer)

    def __init__(self, student_id, assignment_id):
        self.student_id = student_id
        self.assignment_id = assignment_id
        self.grade = 0

    def update_grade(self, new_grade):
        ''' query from student_grade table in db with student_id matching student_id and 
        assignment_id matching assignment_id then takes the max between the grade in 
        database and new_grade, then updates student_grade table with that result '''
        self.grade = max(new_grade, self.grade) 

class Student(db.Model):
    __tablename__ = 'student'

    student_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    email = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    grades = db.relationship('StudentGrade', backref='student', lazy=True)

    def __init__(self, student_id, first_name="Jane", last_name="Doe", 
                 email="general@email.com", password="password"):
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id
        self.email = email
        self.password = password

class QuestionTemplate(db.Model):
    """Question Template which contains a body of text, and variables.

    Attributes:
     data: List of all the variables
     template_file: The JSON file on which this QuestionTemplate is stored.
     template_solution: The JSON file on which the formula is stored.
     body: The body of text for this QuestionTemplate

    """
    __tablename__ = 'question_template'

    id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.String())
    type = db.Column('type', db.String())
    assignment_id = db.Column(db.Integer, db.ForeignKey('assignment.assignment_id'))

    __mapper_args__ = {'polymorphic_on' : type}

    def __init__(self, id, question_text, type, assignment_id):
        """Initializes a QuestionTemplate object."""
        self.id = id
        self.question_text = question_text
        self.type = type
        self.assignment_id = assignment_id

    def get_id(self):
        return self.id

    def question_generator(self):
        """
        Returns a string where the variables are replaced with random values
        """
        variable_pattern="avar *{ *(.) *}"
        fraction_pattern="frac *{ *(.+) *} *{ *(.+) *}"
        formula_pattern="form +(.+)"

       
        all_lines=self.question_text
        is_fraction=False
        #Getting all the variables
        all_vars=findall(variable_pattern,all_lines)
        vars_values=[]
        for var in all_vars:
            vars_values.append(randint(1,10))

        for i in range(0,len(all_vars)):
            exec("%s=%d" % (all_vars[i],vars_values[i]))

        #Getting the fraction
        frac_parts=[]
        frac=findall(fraction_pattern,all_lines)
        if frac:
            is_fraction=True
            frac=list(frac[0])

        for part in frac:
            eq=parser.expr(part).compile()  
            frac_parts.append(eval(eq))
        if is_fraction:
            return(frac_parts[0]/frac_parts[1])

        #Getting the a formula that doesn't contain a fraction
        if not is_fraction:
            form=findall(formula_pattern,all_lines)
            form=''.join(form)
            eq=parser.expr(form).compile()
            return(eval(eq))


        for i in range(0,len(all_vars)):
            self.question_text=re.sub(variable_pattern, str(vars_values[i]), all_lines, count=len(all_vars), flags=0)
    
    def __repr__(self):
        return 'Question %r' % self.id

class MultipleChoice(QuestionTemplate):
    """
    """
    __mapper_arges__ = {'polymorphic_identity': 'Multiple Choice'}
    multipleChoice1 = db.Column(db.String())
    multipleChoice2 = db.Column(db.String())
    multipleChoice3 = db.Column(db.String())
    multipleChoice4 = db.Column(db.String())
    multipleChoice5 = db.Column(db.String())
    correct =  db.Column(db.Integer)


class ShortAnswer(QuestionTemplate):
    """
    """
    __mapper_arges__ = {'polymorphic_identity': 'Short Answer'}

    error_margin = db.Column(db.Integer)


class TrueFalse(QuestionTemplate):
    """
    """
    __mapper_arges__ = {'polymorphic_identity': 'True or False'}

    answer = db.Column(db.Boolean)

    # def __init__(self, answer):
    #     """Initializes an instance of assignment
    #     """
    #     self.answer = answer

class Assignment(db.Model):
    """The Assignment that is designed by the professor, done by the student.

    Attributes:
     id: The id of this assignment
     start_date: The time when this assignment becomes available for
                students. Format: YYYYMMDD
     due_date: The time when this assignment becomes unavailable for students
                 to edit. Format: YYYYMMDD
     grade: The final grade of this assignment.
     question: A list containing all the QuestionTemplates
    """
    __tablename__ = 'assignment'

    assignment_id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    questions = db.relationship('QuestionTemplate', backref='assignment', lazy=True)

    def __init__(self, id, start_date=date(2000, 1, 1),
                 end_date=date(2000, 1, 1)):
        """Initializes an inst an ce of assignment
    """
        self.assignment_id = id
        self.start_date = start_date
        self.end_date = end_date

    def past_due_date(self):
        return self.end_date >= datetime.datetime.now()

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
        for line in self.qt_file:
            qt = QuestionTemplate(body=json.loads(line), solution=json.loads(self.sol_file.readline()))
            qt.question_generator()
            qt.solution_generator()

    def complete_assignment(self):
        grades_file = open("grades/"+str(self.__id)+"grades", 'r')
        grades = grades_file.read().split()
        grades.sort()
        grades_file = open("grades/"+str(self.__id)+"grades", 'w')
        grades_file.write(json.dumps(grades.pop()))

    def save_assignment(self):
        return None

    def __repr__(self):
        return 'Assignment %r' % self.assignment_id
