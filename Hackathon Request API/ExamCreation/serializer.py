from rest_framework import serializers
from .models import Exam,ExamSlot,Center
from CustomUser.models import User

class ExamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exam
        fields = ('name',)


class ExamSlotSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExamSlot
        fields = ('date', 'time')


class CenterSerializer(serializers.ModelSerializer):
    City = serializers.ReadOnlyField(source='city.name')
    class Meta:
        model = Center
        fields = "__all__"



