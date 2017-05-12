from .models import RequestConstraint
from UserRegistration.serializer import RequestConstraintSerializer
from CustomUser.models import User
from rest_framework import generics
from rest_framework import permissions
from ExamCreation.models import Exam

class UserRegistration(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    # def perform_create(self, serializer):
    #     if serializer.data()
    #     serializer.save(owner=self.request.user)