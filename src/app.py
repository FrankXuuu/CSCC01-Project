from datetime import date
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy
import os, csv, io

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.create_all()

#from models import Student
import models

studentProfile = None
professorProfile = None

##########
# VIEWS  #
##########
@app.route('/')
def root():
    return 'Flask is working!'

@app.route('/dashboard', methods=['POST', 'GET'])
def index():
    if (request.method == 'POST'):
        data = request.form['assignment']
        return editAssignmentView(data) 
    elif (request.method == 'GET'):
        assignments = models.Assignment.query.order_by(models.Assignment.assignment_id).all()
        return render_template('index.html', assignments=assignments)

@app.route('/editAssignment', methods=['POST', 'GET'])
def editAssignmentView(data=None):
    error = None
    print(request.method)
    if data:
        assignment = models.Assignment.query.filter_by(assignment_id=data).first()
        questions = models.QuestionTemplate.query.filter_by(assignment_id=data).all()
        return render_template('editAssignment.html', assignment=assignment, questions=questions)
    if (request.method == 'POST'):
        numOfQuestions = len(request.form) - 2
        data = request.form.to_dict(flat=False)
        print(data)
        assignmentID = int(data['assignmentID'][0])
        splitDate = [int(x) for x in data['startDate'][0].split('-')]
        startDate = date(splitDate[0], splitDate[1], splitDate[2])
        splitDate = [int(x) for x in data['endDate'][0].split('-')]
        endDate = date(splitDate[0], splitDate[1], splitDate[2])
        assignment = models.Assignment(
                id = assignmentID,
                start_date = startDate,
                end_date = endDate
            )
        db.session.merge(assignment)
        questions_in_assgn = models.QuestionTemplate.query.filter_by(assignment_id=assignmentID).all()
        for key, value in data.items():
            if not key in ['assignmentID', 'startDate', 'endDate']:
                question = models.QuestionTemplate.query.filter_by(id=int(key)).first()
                if question:
                    questions_in_assgn.remove(question)
                    question.question_text = value[0]
                    db.session.merge(question)
                else:
                    for i, body in enumerate(value):
                        try:
                            question = models.QuestionTemplate(
                                id = models.QuestionTemplate.query.count() + i,
                                question_text = body,
                                solution_formula = 'temp',
                                error_margin = 0,
                                assignment_id = assignmentID
                            )
                            db.session.add(question)
                        except Exception as e:
                            print (e)
                            print ('Couldnt put this question into database')
            db.session.commit()
        deleteQuestionFromDB(questions_in_assgn)
        return redirect(url_for('index'))

def deleteQuestionFromDB(questions):
    for question in questions:
        try:
            question.assignment_id = None
            db.session.merge(question)
        except Exception as e:
            print (e)
            print ('Couldnt delete this line from database')
    db.session.commit()

@app.route('/createAssignment', methods=['POST', 'GET'])
def createAssignmentView():

    error = None
    if (request.method == 'POST'):
        data = request.form.to_dict(flat=False)
        numOfQuestions = int(data['numQuestions'][0])

        if (len(data['assignmentID'][0]) > 0
            and len(data['startDate'][0]) > 0
            and len(data['endDate'][0]) > 0):
            assignmentID = int(data['assignmentID'][0])
            splitDate = [int(x) for x in data['startDate'][0].split('/')]
            startDate = date(splitDate[2], splitDate[0], splitDate[1])
            splitDate = [int(x) for x in data['endDate'][0].split('/')]
            endDate = date(splitDate[2], splitDate[0], splitDate[1])

            assignment = models.Assignment(
                id = assignmentID,
                start_date = startDate,
                end_date = endDate
            )
        else:
            error = 'Fill in all sections'
                
        if not error:
            i = 1
            questions = []
            while (i <= numOfQuestions):
                try:
                    qtype = data['questionType{}'.format(i)][0]
                    if qtype == "True or False":
                        question = models.TrueFalse(
                            id = models.QuestionTemplate.query.count() + i - 1,
                            question_text = data['question{}'.format(i)][0],
                            type = data['questionType{}'.format(i)][0],
                            assignment_id = assignmentID
                                                    )
                        question.answer = (True if ((data['answerTF{}'.format(i)][0]) == 'True') else False)
                        questions.append(question)
                    elif qtype == "Short Answer": 
                        question = models.ShortAnswer(
                            id = models.QuestionTemplate.query.count() + i - 1,
                            question_text = data['question{}'.format(i)][0],
                            type = data['questionType{}'.format(i)][0],
                            assignment_id = assignmentID
                        )
                        question.error_margin = int(data['errorMargin{}'.format(i)][0])
                        questions.append(question)
                    elif qtype == "Multiple Choice": 
                        question = models.MultipleChoice(
                            id = models.QuestionTemplate.query.count() + i - 1,
                            question_text = data['question{}'.format(i)][0],
                            type = data['questionType{}'.format(i)][0],
                            assignment_id = assignmentID
                        )
                        question.multipleChoice1 = data['radioText{}'.format(i)][0]
                        question.multipleChoice2 = data['radioText{}'.format(i)][1]
                        question.multipleChoice3 = data['radioText{}'.format(i)][2]
                        question.multipleChoice4 = data['radioText{}'.format(i)][3]
                        question.multipleChoice5 = data['radioText{}'.format(i)][4]
                        question.correct = int(data['radio{}'.format(i)][0][-1])

                        questions.append(question)
                except Exception as e:
                    print (e)
                    print ('Couldnt put this questions into database')

                


                i += 1
        
            grades = []
            for student in models.Student.query.all():
                try:
                    grade = models.StudentGrade(
                        student_id = student.student_id,
                        assignment_id = assignmentID
                    )
                    grades.append(grade)
                except Exception as e:
                    print (e)
                    print ('Couldnt put grade into database') 
            db.session.add_all([assignment] + questions + grades)
            db.session.commit()
            return redirect(url_for('index'))
    return render_template('createAssignment.html', error=error)

@app.route('/index', methods=['POST', 'GET'])
def studentIndexView():
    if (request.method == 'POST'):
        data = request.form['assignment']
        return assignment(data) 
    elif (request.method == 'GET'):
        assignments = models.Assignment.query.filter(models.Assignment.start_date <= date.today()).order_by(models.Assignment.assignment_id).all()
        global studentProfile
        return render_template('index-student.html', student=studentProfile, assignments=assignments)

@app.route('/class', methods=['POST', 'GET'])
def classView():
    # print("HEREEEE", request.files)
    if (request.method == 'POST'):
        if 'csvFile' not in request.files:
            print("not in request.files")
            return redirect(request.url)
        print("RIGHT HERE")
        csv_file = request.files['csvFile']
        decoded_file = csv_file.read().decode('utf-8')
        io_string = io.StringIO(decoded_file)
        students = []
        grades = []
        assignments = models.Assignment.query.all()
        for row in csv.reader(io_string, delimiter=';', quotechar='|'):
            print(row)
            studentList = row[0].split(',')
            try: 
                student = models.Student(
                    student_id = studentList[0],
                    first_name = studentList[1],
                    last_name = studentList[2],
                    email = studentList[3],
                    password = studentList[4]
                )
                students.append(student)
            except Exception as e:
                print (e)
                print ('Couldnt add student into database')

            for assignment in assignments:
                try:
                    grade = models.StudentGrade(
                        student_id = student.student_id,
                        assignment_id = assignment.assignment_id
                    )
                    grades.append(grade)
                except Exception as e:
                    print (e)
                    print ('Couldnt put grade into database')
        db.session.add_all(students + grades)
        db.session.commit()
        students = models.Student.query.order_by(models.Student.first_name).all()
        return render_template('class.html', students=students)
    elif (request.method == 'GET'):
        students = models.Student.query.order_by(models.Student.first_name).all()
        return render_template('class.html', students=students)

@app.route('/viewGrades', methods=['POST', 'GET'])
def viewGradesView():
    if (request.method == 'POST'):
        data = request.form['assignment']
        return assignment(data) 
    elif (request.method == 'GET'):
        assignments = models.Assignment.query.filter(models.Assignment.start_date <= date.today()).order_by(models.Assignment.assignment_id).all()
        global studentProfile
        return render_template('viewGrades.html', student=studentProfile, assignments=assignments)



# @app.route('/assignment.html')
# def assignmentView():
# 	return render_template('assignment.html')	

@app.route('/dashboard')
def dashboardView():
	return render_template('dashboard.html')

@app.route('/blank')
def blankView():
	return render_template('blank.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if (request.method == 'POST'):
        data = request.form.to_dict(flat=False)
        userEmail = data['userEmail'][0]
        userPassword = data['userPassword'][0]
        student = models.Student.query.filter_by(email=userEmail).first()
        professor = models.Professor.query.filter_by(email=userEmail).first()
        if student:
            if student.password == userPassword:
                global studentProfile
                studentProfile = student
                return redirect(url_for('studentIndexView'))
            else:
                error = 'Incorrect Password'
        elif professor:
            if professor.password == userPassword:
                global professorProfile
                professorProfile = professor
                return redirect(url_for('index'))
            else:
                error = 'Incorrect Password'
        else:
            error = 'Incorrect Email'
    return render_template('login.html', error=error)

@app.route('/register')
def register():
	return render_template('register.html')

@app.route('/forgotPassword')
def forgotPasswordView():
	return render_template('forgot-password.html')

#############
# END VIEWS #
#############

@app.route('/assignment', methods=['POST', 'GET'])
def assignment():
    assignment = None
    questions = None
 
    if (request.method == 'POST'):
        print(request.form)
        data = request.form['assignmentID']
        assignment = models.Assignment.query.filter_by(assignment_id=data).first()
        print(assignment)
    return render_template('assignment.html', assignment=assignment)

@app.route('/assignmentGrade', methods=['POST', 'GET'])
def assignmentGradeView():
    error = None
    if (request.method == 'POST'):
        data = request.form
        print(data)
        global studentProfile
        print (studentProfile)
        correctness = {}
        student_grade = models.StudentGrade.query.filter_by(student_id=studentProfile.student_id, assignment_id=data['assignmentID']).first()
        new_grade = 100
        student_grade.update_grade(new_grade)
        grade = student_grade.grade
        assignment = models.Assignment.query.filter_by(assignment_id=data['assignmentID']).first()
        # db.session.merge(student_grade)
        # db.session.commit()
        pass 
    return render_template('assignmentGrade.html', assignment=assignment, grade=grade)

#############################
# Qestion Template Function #
#############################



if __name__ == '__main__':
	app.run()
