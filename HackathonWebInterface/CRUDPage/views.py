from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.http.response import HttpResponseRedirect, HttpResponseForbidden, HttpResponse
from django.urls import reverse

from APIWebInterface import settings
from AuthPortal.views import logout_user
from ExamCreation.models import Exam,ExamSlot,Center,Vacant
from UserRegistration.models import StudentRequest, CenterAllocated
from .forms import ExamForm,ExamSlotForm,CenterForm
from django.forms import formset_factory
from GeoCoder.views import StartStudentAllocation
from django.utils.encoding import smart_str


def clean_data_(data):
    clean = data.split('^')
    cd = ""
    return data
# TODO  Need to add otp auth else logout the request and redirect to login page
@login_required(login_url='/login/')
def flot(request):
    return render(request, 'CRUDPage/flot/flot.html')

@login_required(login_url='/login/')
def home(request):
    return render(request, 'CRUDPage/dashboard/index.html')

@login_required(login_url='/login/')
def generate(request,name):
    name = clean_data_(name)
    name =clean_data_(name)
    StartStudentAllocation(name)
    exam = Exam.objects.get(name=name)
    Slot = ExamSlot.objects.filter(examid=name)
    return redirect(reverse('crudpage:slot', kwargs={'examid':name + '^'}))



@login_required(login_url='/login/')
def listexam(request):
    Exams = Exam.objects.filter(owner=request.user)
    return render(request,'CRUDPage/exam/exam.html',{'Exams':Exams})


@login_required(login_url='/login/')
def addexam(request):
    if request.method == 'POST':
        form = ExamForm(None)
        context = {
            "form": form,
            "emp_id": 0,
            "title": "Add Exam"
        }
        print(form)
        return render(request, 'CRUDPage/exam/addexam.html',context)


@login_required(login_url='/login/')
def listslot(request, examid, error = None,):
    Sucess = None
    error = None
    try:
        data = examid.split('^')
        if len(data) >= 2:
            examid = data[0]
            Sucess = 'Allocation is sucessfull!!'
        data = examid.split('$')
        if len(data) >= 2:
            examid = data[0]
            error = 'Slots has been assigned'
        if Exam.objects.get(name=examid).owner == request.user:
            exam = Exam.objects.get(name=examid)
            Slot = ExamSlot.objects.filter(examid=examid)
            return render(request, 'CRUDPage/exam/slotlist.html', {'Slots': Slot, 'exam':exam, 'error':error, 'Sucess':Sucess})
        else:
            logout_user(request)
    except:
        logout_user(request)
        pass


@login_required(login_url='/login/')
def slotdetail(request, examid, slotid):
        return HttpResponseForbidden




@login_required(login_url='/login/')
def addslot(request,examid):
    return render(request, 'CRUDPage/formset.html', {'formset':formset,'examid':examid})


@login_required(login_url='/login/')
def addcenter(request, examname):
    form = CenterForm()
    return render(request, 'CRUDPage/generation/centeradd.html', context={})

def getcard(request,slotid,admitno):
    return render(request,'CRUDPage/generation/generation.html',context={})


