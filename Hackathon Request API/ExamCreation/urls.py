from django.conf.urls import url
from ExamCreation.views import CenterList
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns=[
    url(regex='^add/$', view=CenterList.as_view()),
]
urlpatterns=format_suffix_patterns(urlpatterns)