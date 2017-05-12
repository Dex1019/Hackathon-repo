from django.db import models
from CustomUser.models import User


class Exam(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=500,unique=True)
    registrationStartDate = models.DateTimeField()
    registrationEndDate = models.DateTimeField()
    days = models.IntegerField()
    slots = models.IntegerField()
    owner = models.ForeignKey(User, related_name='Exam')

    class Meta:
            ordering=('created',)

    def __str__(self):
        return self.name


class Center(models.Model):
    name = models.CharField(max_length=500)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    capicity = models.IntegerField()
    examid = models.ForeignKey(Exam)

    class Meta:
        ordering=('state','city')

    def __str__(self):
        return self.name


class ExamSlot(models.Model):
    examid = models.ForeignKey(Exam)
    slotid = models.TextField(max_length=1000,primary_key=True)
    centerid = models.ForeignKey(Center)
    date = models.DateField()
    time = models.TimeField()
    vaccant = models.IntegerField(default=0)

    def __str__(self):
        return  self.Slotid