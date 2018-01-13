from app import db, app
from sqlalchemy.dialects.postgresql import JSON

#from assignment import Assignment
from datetime import date

import json

from .. import models


class Student(db.Model):
    __tablename__ = 'student'

    student_id = db.Column(db.String(10), primary_key=True)
    first_name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    

    def __init__(self, student_id="0", first_name="Jane", last_name="Doe", 
                 email="general@email.com", password="password"):
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id
        self.finalGrade = 0
        # [0] * n will create a list of length n and all elements are 0
        self.assignment_grades = []
        self.avaiable_assignments = []
        self.current_working_assignment = None

    def startAssignment(self, assignment_id):
        try:
            self.avaiable_assignments.index(assignment_id)
            self.current_working_assignment = Assignment(id=assignment_id)
            open("studentSol/"+str(assignment_id)+"assignment_sol.json", 'a')
            self.current_working_assignment.generate_assignment()
        except ValueError:
            print("You can't work on this assignment!")

    def redo_assignment(self, assignment_id):
        startAssignment(assignment_id)

    def submitAssignment(self, assignment_id=0):
        grade = self.current_working_assignment.grade_assignment()
        print(grade)

    def getName(self):
        return "{} {}".format(self.firstName, self.lastName)

    def getStudentID(self):
        return self.studentID

    def getFinalGrade(self):
        return self.finalGrade

    def getAssignmentGrades(self):
        return self.assignmentGrades

    def setAssignmentGrade(self, assignmentNumber, grade):
        self.assignmentGrades[assignmentNumber] = grade
        self.finalGrade = (float(sum(self.assignmentGrades)) /
                           len(self.assignmentGrades))

    def get_available_assignments(self):
        today = date.today()
        directory_file = open("directory.json", 'r')
        for line in directory_file:
            a_id = json.loads(line)
            start = json.loads(directory_file.readline()).split()
            end = json.loads(directory_file.readline()).split()
            start_date = date(int(start[0]), int(start[1]), int(start[2]))
            due_date = date(int(end[0]), int(end[1]), int(end[2]))
            if (today <= due_date and start_date <= today):
                self.avaiable_assignments.append(a_id)

