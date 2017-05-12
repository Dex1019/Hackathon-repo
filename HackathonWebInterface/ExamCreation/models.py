from django.db import models
from CustomUser.models import User


class Exam(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=500,primary_key=True)
    registrationStartDate = models.DateTimeField()
    registrationEndDate = models.DateTimeField()
    days = models.IntegerField()
    slots = models.IntegerField()
    owner = models.ForeignKey(User, related_name='Exam')

    class Meta:
            ordering=('created',)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=1000)
    def_long = models.FloatField()
    def_lat = models.FloatField()

    def __str__(self):
        return (self.name)


class Center(models.Model):
    name = models.CharField(max_length=500)
    city = models.ForeignKey(City)
    state = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name


class ExamSlot(models.Model):
    examid = models.ForeignKey(Exam, related_name='exam')
    slotid = models.TextField(max_length=1000,primary_key=True)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.slotid

class Vacant(models.Model):
    slotid = models.ForeignKey(ExamSlot)
    centerid = models.ForeignKey(Center)
    avl_seats = models.IntegerField()
    capicity = models.IntegerField()

    def __str__(self):
        return (self.slotid.slotid + "-" + self.centerid.name)


