"""CiscoStudents URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from ciscoapp import views
from django.conf import settings
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),

	path('', views.index, name='index'),
	path('view_students', views.get_students, name='get_students'),
	path('studentsByRange', views.searchStudentsByRange, name='searchStudentsByRange'),
    path('inputStudentRange', views.inputStudentRange, name='inputStudentRange'),
    path('insertStudentHtml', views.insertStudentHtml, name='insertStudentHtml'),
	path('insertStudent', views.insertStudent, name='insertStudent'),
	path('deleteStudentHtml', views.deleteStudentHtml, name='deleteStudentHtml'),
	path('deleteStudent', views.deleteStudent, name='deleteStudent'),
	path('updateStudentHtml', views.updateStudentHtml, name='updateStudentHtml'),
	path('updateStudent', views.updateStudent, name='updateStudent'),
	path('loginStudentHtml', views.loginStudentHtml, name='loginStudentHtml'),
	path('Login', views.Login, name='Login'),
	path('subchpHtml', views.subchpHtml, name='subchpHtml'),
	path('subchp', views.subchp, name='subchp'),
	path('retrieve', views.retrieve, name='retrieve'),
	path('viewBank', views.viewBank, name='viewBank'),
    path('enterBank', views.enterBank, name='enterBank'),
	path('dashboardS.html', views.dashboardS, name='dashboardS'),
	path('accounts/', include('django.contrib.auth.urls')),
	#path('QuestionOfTheWeekS.html', views.subSelect, name='QuestionOfTheWeekS.html'),
	#path('QuestionBank.html', views.subSelect, name='QuestionBank.html'),
	path('testModal', views.testModal, name='testModal'),
    path('enter_questions', views.enterBank, name='enter_questions'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('', TemplateView.as_view(template_name='index.html'), name='homepage'),
    path('QuestionOfTheWeekS.html', views.QuestionOfTheWeekS, name='QuestionOfTheWeekS')
    #path('view_school', views.get_school, name='get_school'),
]
