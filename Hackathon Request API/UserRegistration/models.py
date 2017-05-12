from django.db import models
from CustomUser.models import User
from ExamCreation.models import ExamSlot, Exam, Center, City


class StudentRequest(models.Model):
    owner = models.ForeignKey(User)
    slotid = models.ForeignKey(ExamSlot)
    admitid = models.CharField(max_length=100, primary_key=True)
    longitude = models.FloatField(default=0)
    latitude = models.FloatField(default=0)
    city = models.CharField(max_length=100,)
    state = models.CharField(max_length=100,)
    requestdatetime = models.DateTimeField(auto_now=True)
    allocated = models.BooleanField(default=False)
    is_handicap = models.BooleanField(default=False)
    is_female = models.BooleanField(default=False)
    name = models.CharField(max_length=100)
    fathername = models.CharField(max_length=100)
    class Meta:
        ordering = ('is_handicap','is_female','requestdatetime')

    def __str__(self):
        return self.slotid.slotid + self.admitid




class RequestConstraint(models.Model):
    owner = models.ForeignKey(User)
    requestdate = models.DateField(auto_now_add=True)
    examname = models.CharField(max_length=500, unique=True)
    longitude = models.FloatField()
    latitude = models.FloatField()
    admitid = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    fathername = models.CharField(max_length=100,default='Samurai jack')
    name = models.CharField(max_length=100,default='Manav')
    is_handicap = models.BooleanField(default=False)
    is_female = models.BooleanField(default=False)

    class Meta:
        ordering=('requestdate',)

class CenterAllocated(models.Model):
    examname = models.ForeignKey(Exam,related_name='examname')
    admitno = models.ForeignKey(StudentRequest,related_name='admitno')
    centerid = models.ForeignKey(Center,related_name='centerid')


    def __str__(self):
        return self.admitno.admitid