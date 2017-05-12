import rest_framework

from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^center/',include('ExamCreation.urls')),
    url(r'^' , include('UserRegistration.urls')),
]

urlpatterns += [url(r'api-auth/',include('rest_framework.urls'),name='rest_framework'),]
