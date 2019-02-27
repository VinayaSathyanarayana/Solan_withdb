from django.db import connection
from django.contrib.auth.models import User, Group
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django import template
#from sqlalchemy.sql import text

# Create your views here.

from django.contrib.auth import authenticate, logout,login
from .models import Student
from .models import login
from .models import question
from .models import subject
from .models import points

register = template.Library()
@register.filter(name='has_group')
def has_group(user, group_name):
    group = Group.objects.get(name=group_name)
    return True if group in user.groups.all() else False



def index(request):
    #return HttpResponse('hello, you are at the polls index')
    return render(request, 'ciscoapp/home.html')


def get_students(request):
    print ("get_students")
    st_lst =  Student.objects.all()
    print (str(st_lst))
    context_dict = {}
    return render(request, 'ciscoapp/view_students.html', {'st_lst': st_lst})


def searchStudentsByRange(request):
    startingRoll = request.POST['startRoll']
    endRoll = request.POST['endRoll']
    print ("startingRoll is " + str(startingRoll))
    print ("endRoll is " + str(endRoll))
    #st_lst = Student.objects.filter(roll_nbr__gte=startingRoll, roll_nbr__lte=endRoll)
    st_lst = Student.objects.raw('select * from students where roll_nbr between ' + str(startingRoll) + ' and ' + str(endRoll) )
    return render(request, 'ciscoapp/view_students.html', {'st_lst': st_lst})


def inputStudentRange(request):
    st_lst =  Student.objects.all()
    return render(request, 'ciscoapp/enter_range.html', {'st_lst': st_lst})


def insertStudentHtml(request):
    return render(request, 'ciscoapp/insert_student.html')


def insertStudent(request):
    rollNbr = request.POST['rollNbr']
    studentName = request.POST['studentName']
    subject = request.POST['subject']
    standard = request.POST['standard']
    args = (rollNbr,studentName,subject,standard)
    query = "INSERT INTO students(roll_nbr, student_name, subject, standard) " \
            "VALUES(%s,%s, %s, %s)"
    #student1 = Student(roll_nbr=rollNbr, student_name=studentName, subject=subject, standard=standard)
    #student1.save()
    cursor = connection.cursor()
    cursor.execute(query,args)
    #cursor.close()
    st_lst = Student.objects.raw('select * from students')
    return render(request, 'ciscoapp/view_students.html', {'st_lst': st_lst})


def deleteStudentHtml(request):
    return render(request, 'ciscoapp/delete_student.html')


def deleteStudent(request):
    rollNbr1=request.POST['rollNbr1']
    print('roll number is :' + str(rollNbr1))
    args=(rollNbr1,)
    query = " DELETE FROM students WHERE roll_nbr=%s "
    #Student.objects.raw('delete from students where roll_nbr =' + str(rollNbr))
    cursor = connection.cursor()
    cursor.execute(query, args)
    st_lst = Student.objects.raw('select * from students')
    return render(request, 'ciscoapp/view_students.html', {'st_lst': st_lst})


def updateStudentHtml(request):
    return render(request, 'ciscoapp/update_student.html')


def updateStudent(request):
    rollNbr2 = request.POST['rollNbr2']
    studentName = request.POST['studentName']
    print('roll number is :' + str(rollNbr2))
    args=(studentName,rollNbr2)
    query = "UPDATE students SET student_name = %s WHERE roll_nbr = %s"
    cursor = connection.cursor()
    cursor.execute(query,args)
    st_lst = Student.objects.raw('select * from students')
    return render(request, 'ciscoapp/view_students.html', {'st_lst': st_lst})


def loginStudentHtml(request):
    return render(request, 'ciscoapp/login_student.html')


def Login(request):
    email=request.POST['email']
    password=request.POST['password']
    #args=(email,password)
    #query="select * from login where email_id=%s and password=%s"
    #cursor=connection.cursor()
    #cursor.execute(query,args)
    login_lst = login.objects.raw("select * from login where email_id= " + "'" + str(email) + "'" + " and password=" + "'" + str(password) + "'")
    print(login_lst)
    #return render(request, 'ciscoapp/view_students.html', {'login_lst': login_lst})
    if login_lst != None:
        return HttpResponse('you have logged in successfully!')
    else:
        return render(request, 'ciscoapp/view_students.html', {'login_lst': login_lst})
    #user = authenticate(username=email, password=password)
    #print(user)
    #if user :
    #    login(request,user)
    #    return HttpResponse('you have logged in successfully!')
    #else:
    #    return HttpResponse('have you forgotten your password?')


def subchpHtml(request):
    return render(request, 'ciscoapp/sub_chp.html')

def subchp(request):
    sub=request.POST['sub']
    chp=request.POST['chp']
    print('subject is : ', str(sub))
    print(' is : ', str(chp))
    args=(sub,chp)
    query = 'select sub from subject'
    cursor = connection.cursor()
    cursor.execute(query,args)
    sub_chp_lst = Subject.objects.raw('select sub from subject')
    return render(request, 'ciscoapp/sub_chp.html', {'sub_chp_lst': sub_chp_lst})

def retrieve(request):
	print ("get_students")
	q_lst =  questions.objects.all()
	print (str(q_lst))
	context_dict = {}
	return render(request, 'ciscoapp/QuestionBank.html', {'q_lst': q_lst})

def dashboardS(request):
    query_result1 = points.objects.filter(
        login__user__email=str(request.user.email))
    pointsObject = query_result1[0]
    query = "select * from point order by points DESC LIMIT 5"
    print(query)
    query_result5 = points.objects.raw(query)
    print(query_result5)
    #return render(request, 'ciscoapp/dashboardS.html', {'query_results': query_results})
    return render(request, 'ciscoapp/dashboardS.html', {'query_results': query_result5, 'pointsObject': pointsObject})
    #desc return render(request, 'ciscoapp/dashboardS.html', {'pointsObject': pointsObject})

def dashboardT(request):
    return render(request, 'ciscoapp/dashboardT.html')




def homepage(request):
    return render(request, 'ciscoapp/index.html')

def viewBank(request):
    subject=request.POST.get('myselect1')
    chapter=request.POST.get('myselect2')
    if chapter == "All":
        print('subject is : ', str(subject))
        print('chapter is : ', "All Questions")
        query = "select * from question where subject = " + "'" + str(subject) + "'"
    else:
        print('subject is : ', str(subject))
        print('chapter is : ', str(chapter))
        query = "select * from question where subject = " + "'" + str(subject) + "'" + " and chapter = " + "'" + str(chapter) + "'"
    questions = question.objects.raw(query)
    return render(request, 'ciscoapp/QuestionBank.html', {'questionList': questions})


def testModal(request):
    return render(request, 'ciscoapp/test_modal.html',{})


def enterBank(request):
    subject1 = request.POST.get('myselect3')
    chapter1 = request.POST.get('myselect4')
    question1 = request.POST['questionID']
    username1 = request.POST['username']
    print(type(question1))
    print(type(subject1))
    print(type(chapter1))
    args = (subject1, chapter1, question1)
    print('subject is : ', str(subject1))
    print('chapter is : ', str(chapter1))
    print('question is : ', str(question1))
    # print('type is : ', str(type))
    # question=request.POST.get('subjective')
    #query = "INSERT INTO question(subject,chapter,question) " \
    #       "VALUES(%s,%s,%s)"
    query = "insert into question VALUES " +  "(" + "'" + str(subject1) + "'" + "," + "'" + str(chapter1) + "'" + "," + "'" + str(question1) + "'" + ","  + "'" + "n" + "'" + "," + "'" + str(username1) + "'" + ")"
    #query = "insert into question VALUES " + "(" + "'" + str(subject1) + "'" + "," + "'" + str(chapter1) + "'" + ")"
    #query1 = "insert into question VALUES(%s) where subject = " + "'" + str(subject1) + "'" + " and chapter = " + "'" + str(chapter1) + "'"
    print(query)
    cursor = connection.cursor()
    cursor.execute(query)
    query_result1 = points.objects.filter(login__user__email=str(request.user.email))
    pointsObject = query_result1[0]
    pointsObject.points += 1
    pointsObject.save()
    st_lst = question.objects.raw('select * from question')
    return render(request, 'ciscoapp/enter_questions.html', {'st_lst': st_lst})
    #questions = question.objects.raw(query)
    # return render(request, 'ciscoapp/dashboardS.html')

"""def QuestionOfTheWeekS(request):
    st_lst = Student.objects.raw("select question from question where subject = 'Chemistry' and chapter = 'Kinetics' ")
    return render(request, 'ciscoapp/view_students.html', {'st_lst': st_lst})"""


def student_q_manage(request):

    subject = request.POST.get('myselect1')
    chapter = request.POST.get('myselect2')
    print('subject is : ', str(subject))
    print('chapter is : ', str(chapter))
    request.session['subject23'] = subject
    request.session['chapter23'] = chapter
    request.session['subject53'] = subject
    request.session['chapter53'] = chapter
    query = "select * from question where subject = " + "'" + \
        str(subject) + "'" + " and chapter = " + "'" + str(chapter) + "'"
    questions = question.objects.raw(query)
    return render(request, 'ciscoapp/B1.html', {'questionList': questions})


def myquestions(request):
    username = request.POST
    print('Username is : ', str(subject))
    print('chapter is : ', str(chapter))
    request.session['subject23'] = subject
    request.session['chapter23'] = chapter
    request.session['subject53'] = subject
    request.session['chapter53'] = chapter
    query = "select * from question where username = " + "'" + \
        str(username) + "'" 
    questions = question.objects.raw(query)
    return render(request, 'ciscoapp/B5.html', {'questionList': questions})

def GenReport(request):
    # grade = request.POST.get('myselect3')
   # section = request.POST.get('myselect4')
    # query = "select * from points where grade = " + "'" + grade +"'"+"and section = " + "'" + str(section) + "'"
    #points = points.objects.raw(query)
    query = "select * from point order by points DESC "
    query_results = points.objects.raw(query)
    return render(request, 'ciscoapp/GenReport.html', {'query_results': query_results})


def editquestion(request):
    question2 = request.POST['question123']
    #request.session['question33'] = question2
    print('question2 is : ', str(question2))
    question5 = request.POST['question456']
    subject23 = request.session['subject23']
    chapter23 = request.session['chapter23']
    #return render(request, 'ciscoapp/Edit Question.html')
    #request.session['question2'] = question2
    print('question5 is : ', str(question5))
    query = "update question set  question = " + "'" + \
        str(question5) + "'" + " where question = " + \
        "'" + str(question2) + "'" + "and subject = " + "'" + str(subject23) + "'" + " and chapter = " + "'" + str(chapter23) + "'"
    print(query)
    questions = question.objects.raw(query)
    args = (question2,question5)
    cursor = connection.cursor()
    #cursor.execute("update question set question = (%s) where question = (%s) ", args)
    cursor.execute(query)
    return render(request, 'ciscoapp/enter_questions.html')


def deletequestion(request):
    question9 = request.POST['question333']
    print(question9)
    subject33 = request.session['subject23']
    chapter33 = request.session['chapter23']
    query = "delete from  question where question = " + \
        "'" + str(question9) + "'" + "and subject = " + "'" + str(subject33) + \
        "'" + " and chapter = " + "'" + str(chapter33) + "'"
    print(query)
    cursor = connection.cursor()
    cursor.execute(query)
    return render(request, 'ciscoapp/Deletequestion.html')


def questionoftheweekstudent(request):
	#query = "select * from question where qotw ='y'"
    query = "select * from qotw "
    print(query)
    question234 = question.objects.raw(query)
    return render(request, 'ciscoapp/QuestionoftheweekS.html', {'questionList': question234})

def qotwstudent(request):
    studans = request.POST['studans']
    query = "select * from  qotw  "
    print(query)
    questions = question.objects.raw(query)
    return render(request, 'ciscoapp/qotwsubmit.html', {'questionList': questions, 'studans': studans})

def questionoftheweekteacher(request):
    question11 = request.POST['question111']
    subject43 = request.session['subject23']
    chapter43 = request.session['chapter23']
    print(question11)

    request.session['question112'] = question11
    request.session['subject112'] = subject43
    request.session['chapter112'] = chapter43
    #query = "update question set  qotw = " + "'" + \
        #str('y') + "'" + " where question = " + \
       # "'" + str(question11) + "'" + "and subject = " + "'" + str(subject43) + \
        #"'" + " and chapter = " + "'" + str(chapter43) + "'"
    #cursor = connection.cursor()
    #cursor.execute(query)
    query = "select * from question where question = " + "'" + \
        str(question11) + "'" + "and subject =" + "'" + str(subject43) + "'" + "and chapter =" + "'" + str(chapter43) + "'"
    print(query)
    questions = question.objects.raw(query)
    return render(request, 'ciscoapp/qotw.html', {'question1123': questions})
    print(question1123)


def qotw(request):
    question112 = request.session['question112']
    subject113 = request.session['subject112']
    chapter113 = request.session['chapter112']
    opt1 = request.POST['option1']
    opt2 = request.POST['option2']
    opt3 = request.POST['option3']
    opt4 = request.POST['option4']
    ans = request.POST['ans']
    print(question112)
    print(opt1)
    print(opt2)
    query123= "delete from qotw"
    print(query123)
    query = "insert into qotw VALUES " + "(" + "'" + str(subject113) + "'" + "," + "'" + str(chapter113) + "'" + "," + \
     "'" + str(question112) + "'" + "," + "'" + str(opt1) + "'" + "," + "'" + str(opt2) + "'" + "," + "'" + str(opt3) + \
        "'" + "," + "'" + str(opt4) + "'" + "," + "'" + str(ans) + "'" + ")"
    print(query)
    cursor = connection.cursor()
    cursor.execute(query123)
    cursor.execute(query)

    return render(request, 'ciscoapp/enter_questions.html')


def rightans(request):
    query_result1 = points.objects.filter(
        login__user__email=str(request.user.email))
    pointsObject = query_result1[0]
    pointsObject.points += 1
    pointsObject.save()
    return render(request, 'ciscoapp/qotwsubmit1.html')


def wrongans(request):
    query_result1 = points.objects.filter(
        login__user__email=str(request.user.email))
    pointsObject = query_result1[0]
    pointsObject.points += 0
    pointsObject.save()
    return render(request, 'ciscoapp/qotwsubmit1.html')
def QuestionOfTheWeekS(request):
    query = "select * from  qotw  "
    print(query)
    questions = question.objects.raw(query)
    return render(request, 'ciscoapp/QuestionoftheweekS.html', {'questionList': questions})


def questions(request):
    return render(request, 'ciscoapp/QuestionoftheweekS.html')


'''def updatequestion(request):
    question4 = request.session['question2']
    print('question4 is : ', str(question4))
    question3 = request.POST['questionnew']
    print('question3 is : ', str(question3))
    query = "update question set  question = " + "'" + \
        str(question3) + "'" + " where question = " + "'" + str(question4) + "'"
    questions = question.objects.raw(query)


    args = (question3)
    cursor = connection.cursor()
    cursor.execute("update question set question = (%s) where question = () ", args)
    st_lst = question.objects.raw('select * from question')
    return render(request, 'ciscoapp/enter_questions.html', {'st_lst': st_lst})'''


