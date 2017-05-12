from rest_framework import serializers
from rest_framework import status
from ExamCreation.models import Exam
from .models import CenterAllocated
from UserRegistration.serializer import RequestConstraintSerializer,CenterAllocatedSerializer
from CustomUser.models import User
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view


class StudentRequestConstraint(generics.CreateAPIView):
    serializer_class = RequestConstraintSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


@api_view(['GET'])
def CenterAllocatedRequest(request,examid,admitid,format=None):
    """ Retrives the value and sends and modified it"""

        examname = Exam.objects.get(name=examid)
        allocated = CenterAllocated.objects.filter(examname=examname)
        allocated = allocated.get(admitno=admitid)
    if request.method == 'GET':
        serializer = CenterAllocatedSerializer(allocated)
        return Response(serializer.data)