from rest_framework import status, permissions
from .models import Exam,ExamSlot,Center
from .serializer import ExamSerializer,ExamSlotSerializer,CenterSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view


class ExamList(generics.ListAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer


@api_view(['GET'])
def ExamSlotList(request,examid, format=None):
    """ Retrives the exam slot"""
    try:
        examname = Exam.objects.get(name=examid)
        slot = ExamSlot.objects.filter(examid=examname)
    except ExamSlot.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    except Exam.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ExamSlotSerializer(slot,many=True)
        return Response(serializer.data)

class CenterList(generics.CreateAPIView):
    serializer_class = CenterSerializer
    permission_classes = (permissions.IsAuthenticated,)
