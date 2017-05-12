from rest_framework import serializers
from .models import RequestConstraint,StudentRequest, CenterAllocated
from CustomUser.models import User
from ExamCreation.models import Exam, ExamSlot


class RequestConstraintSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    def validate(self, attrs):

        examname = attrs['examname']
        date = attrs['date']
        time = attrs['time']
        slotid = examname + str(date) + str(time)
        try:
            ExamSlot.objects.filter(slotid=slotid)[0]
        except:
            raise serializers.ValidationError("Please check your examname, date and time.")
        try:
            if StudentRequest.objects.filter(slotid=slotid).get(admitid=attrs['admitid']).admitid:
                raise serializers.ValidationError("Admit No already exists")
        except StudentRequest.DoesNotExist:
            return attrs

    class Meta:
        model = RequestConstraint
        fields = ('owner','name','fathername', 'examname', 'date', 'time', 'longitude', 'latitude', 'admitid','city','state','is_handicap','is_female')

    # def create(self, validated_data):
    #     return RequestConstraint(**validated_data)
    def save(self, **kwargs):
        owner = kwargs.get('owner')
        exams = Exam.objects.filter(owner=owner)
        check = exams.get(name=self.validated_data['examname']).name
        examname = self.validated_data['examname']
        date = self.validated_data['date']
        time = self.validated_data['time']
        name = self.validated_data['name']
        fathername = self.validated_data['fathername']
        latitide = self.validated_data['latitude']
        longitude = self.validated_data['longitude']
        admitid = self.validated_data['admitid']
        city = self.validated_data['city']
        state = self.validated_data['state']
        slotid = examname + str(date) + str(time)
        slotid = ExamSlot.objects.get(slotid=slotid)
        is_hadicap = self.validated_data['is_handicap']
        is_female = self.validated_data['is_female']
        student = StudentRequest(owner=owner,slotid=slotid,admitid=admitid,longitude=longitude,latitude=latitide,city=city,state=state,is_female=is_female,is_handicap=is_hadicap,name=name,fathername=fathername)
        student.save()

class CenterAllocatedSerializer(serializers.ModelSerializer):


    examname = serializers.ReadOnlyField(source='examname.name')
    admitno = serializers.ReadOnlyField(source='admitno.admitid')
    latitude = serializers.FloatField(source='centerid.latitude')
    longitude = serializers.FloatField(source='centerid.longitude')
    centername = serializers.CharField(source='centerid.name')
    city = serializers.ReadOnlyField(source='centerid.city.name')
    state = serializers.CharField(source='centerid.state')
    class Meta:
        model = CenterAllocated
        fields = ('examname', 'admitno', 'centername', 'latitude', 'longitude','city','state')
