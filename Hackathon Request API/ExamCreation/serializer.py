from rest_framework import serializers
from .models import Exam,ExamSlot,Center
from CustomUser.models import User

class ExamSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Exam
        fields = ('name', 'registrationStartDate', 'registrationEndDate', 'days', 'slots', 'owner')


