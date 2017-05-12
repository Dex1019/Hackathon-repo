from django import forms
from ExamCreation.models import Exam, ExamSlot, Center
from Student.models import StudentDetail

class StudentDetailForm(forms.ModelForm):
    class Meta:
        model = StudentDetail
        exclude = ('owner',)
