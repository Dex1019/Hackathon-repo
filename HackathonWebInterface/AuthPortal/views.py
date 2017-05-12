from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from CustomUser.models import User
from django.http.response import HttpResponse, HttpResponseRedirect

# Create your views here.
from AuthPortal.forms import UserForm,LoginForm

#  Need to check for password


def index(request):
    return render(request, 'AuthPortal/portal.html')


def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        users = User.objects.all()
        if form.is_valid():

            user = form.save(commit=False)
            password = form.cleaned_data['password']
            # Checking exsiting website
            if users.filter(website=form.cleaned_data['website']).count():
               return render(request, 'AuthPortal/portal.html', {
                    'form': form,
                    'error': 'Website already exists',
                    'signup': True,
                })
            #  Checking if phone number exists
            if users.filter(phonenumber=form.cleaned_data['phonenumber']).count():
               return render(request, 'AuthPortal/portal.html', {
                    'form': form,
                    'error': 'Phone number already exists',
                    'signup': True,
                })
            #  Checking if email exists
            if users.filter(email=form.cleaned_data['email']).count():
                return render(request, 'AuthPortal/portal.html', {
                    'form': form,
                    'error': 'Email already exists',
                    'signup': True,
                })
            # TODO Use the regex to do password validation

            #  If every thing is correct then save the password and the user
            user.set_password(password)
            user.save()
            # TODO  Set the trigger
            return render(request, 'AuthPortal/portal.html')
        elif form.has_error('email'):
           return render(request, 'AuthPortal/portal.html', {
                    'form': form,
                    'error': 'Enter correct Email address',
                    'signup': True,
            })
        elif form.has_error('username'):
            return render(request, 'AuthPortal/portal.html', {
                'form': form,
                'error': 'Username already exists',
                'signup': True,
            })
        else:
            return render(request, 'AuthPortal/portal.html', {'signup': True, 'form':form})
    else:
        return render(request, 'AuthPortal/portal.html', {'signup': True})


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        # TODO USe the email trigger to authenticate. Redirect to OTP page
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/listexam/')
            else:
                return render(request, 'AuthPortal/portal.html',
                              {'form': form, 'error_message': 'Your Account is blocked'})
        else:
            return render(request, 'AuthPortal/portal.html',
                          {'form': form, 'error_message': 'Incorrect Credential',})

    return render(request, 'AuthPortal/portal.html')


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/login/')
