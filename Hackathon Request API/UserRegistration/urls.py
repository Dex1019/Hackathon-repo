from django.conf.urls import url
from UserRegistration import views
from ExamCreation.views import ExamList,ExamSlotList
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns=[
    # url for the projects
    url(regex='^register/$', view=views.StudentRequestConstraint.as_view()),
    url(regex=r'^getcenter/(?P<examid>.*)/(?P<admitid>.*)/$',view=views.CenterAllocatedRequest),
    url(regex=r'^listexam/$', view=ExamList.as_view()),
    url(regex=r'^listexam/(?P<examid>.*)/$',view=ExamSlotList),
]

urlpatterns=format_suffix_patterns(urlpatterns)