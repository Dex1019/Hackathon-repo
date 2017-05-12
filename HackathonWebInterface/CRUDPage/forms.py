from django import forms
from ExamCreation.models import Exam, ExamSlot, Center


class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        exclude = ('owner',)


class ExamSlotForm(forms.ModelForm):
    class Meta:
        model = ExamSlot
        fields = ( 'date', 'time')

class CenterForm(forms.ModelForm):
    class Meta:
        model = Center
        fields = ('name','latitude','longitude')

# class VacantForm(forms.ModelForm):
#     choices = Center.objects.all()
#     Choic = []
#     for i in choices:
#         Choic.append(i.name)
#
#     Choices = tuple(Choic)
#
#     class Meta:
#
#
#     class Meta:
#         model = Vacant
#
