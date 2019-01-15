from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.utils import timezone
# Create your models here.



class Student(models.Model):
    roll_nbr = models.IntegerField(primary_key=True,default = 0, db_column='roll_nbr', null=False)
    student_name = models.CharField(max_length=30, db_column = 'student_name', null = False)
    subject = models.CharField(max_length=20)
    standard = models.IntegerField(default = 0, db_column='standard')

    class Meta:
        db_table = 'students'
        verbose_name_plural = 'students'
        
    def __str__(self):
        return str(self.roll_nbr) + ' Name => ' + str(self.student_name)

class login(models.Model):
    #email_id = models.CharField(max_length=50, db_column='email_id', null= False)
    #password = models.CharField(max_length=50, db_column='password', null= False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    class Meta:
        db_table = 'login'
        verbose_name_plural = 'logins'

    def __str__(self):
        return str(self.id)

class subject(models.Model):
    sub=models.CharField(max_length=50, db_column='sub', null=False)
    chp=models.CharField(max_length=25, db_column='chp', null=True)

    class Meta:
        db_table = 'subject'
        verbose_name_plural = 'subjects'

    def __str__(self):
        return str(self.id)

class question(models.Model):
    subject=models.CharField(primary_key=True,max_length=80,db_column='subject', null=False)
    chapter=models.CharField(max_length=80,db_column='chapter', null=False)
    question=models.CharField(max_length=1000, db_column = 'question', null = False)
    qotw = models.CharField(max_length=1, db_column='qotw', default='n')
    class Meta:
        db_table = 'question'
        verbose_name_plural = 'questions'

class qotw(models.Model):
    subject=models.CharField(primary_key=True,max_length=80,db_column='subject', null=False)
    chapter=models.CharField(max_length=80,db_column='chapter', null=False)
    question=models.CharField(max_length=1000, db_column = 'question', null = False)
    option1 = models.CharField(max_length=500, db_column='option1', null=False)
    option2 = models.CharField(max_length=500, db_column='option2', null=False)
    option3 = models.CharField(max_length=500, db_column='option3', null=False)
    option4 = models.CharField(max_length=500, db_column='option4', null=False)
    ans = models.CharField(max_length=5,db_column='ans', null=False)
    class Meta:
        db_table = 'qotw'
        verbose_name_plural = 'qotw'

class points(models.Model):
    points = models.IntegerField(default=0, db_column='points', null=False)
    login = models.ForeignKey(login, on_delete=models.CASCADE)
    #username=models.CharField(max_length=80,db_column='username', null=False) #display usernames
    #grade=models.IntegerField(default=10,db_column='grade', null=False)
    #section=models.CharField(max_length=1,default='A',db_column='grade', null=False)

    class Meta:
        db_table = 'point'
        verbose_name_plural = 'points'




