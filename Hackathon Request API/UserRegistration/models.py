from django.db import models
from CustomUser.models import User
from ExamCreation.models import ExamSlot


class StudentRequest(models.Model):
    owner = models.ForeignKey(User)
    slotid = models.ForeignKey(ExamSlot)
    admitid = models.CharField(max_length=100)
    longitude = models.FloatField()
    latitude = models.FloatField()
    requestdate = models.DateField()

    class Meta:
        ordering=('requestdate',)

class RequestConstraint(models.Model):
    owner = models.ForeignKey(User)
    requestdate = models.DateField(auto_now_add=True)
    examname = models.CharField(max_length=500, unique=True)
    longitude = models.FloatField()
    latitude = models.FloatField()
    date = models.DateField()
    time = models.TimeField()
    class Meta:
        ordering=('requestdate',)