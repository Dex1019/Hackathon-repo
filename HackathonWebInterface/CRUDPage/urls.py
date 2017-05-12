from django.conf.urls import url,include
from .views import  home,flot,listexam,getcard,addexam,listslot,slotdetail,addslot,addcenter,generate
app_name='crudpage'

urlpatterns = [
    url(r'^home/$', home, name="home"),
    url(r'^generate/(?P<name>.*)/$', generate, name="generate"),
    url(r'^getcard/(?P<slotid>.*)/(?P<admitno>.*)$', getcard, name="getcard"),
    #url(r'^downloadcard/(?P<slotid>.*)/(?P<admitno>.*)$', download, name="download"),
    url(r'^flot/$', flot, name="flot"),
    url(r'^listexam/$', listexam, name="exam"),
    url(r'^exam/addcenter/(?P<examname>.*)/$',addcenter,name="addcenter"),
    url(r'^exam/(?P<examid>.*)/addslots/$', addslot, name="addslot"),
    url(r'^exam/(?P<examid>.*)/(?P<slotid>.*)/$', slotdetail, name="slotdetail"),
    #url(r'^exam/addcenter/(?P<examname>.*)/$',addcenter,name="addcenter"),
    url(r'^exam/(?P<examid>.*)/$', listslot, name="slot"),
    url(r'^addexam/$',addexam,name = "addexam"),
    #url(r'listexam/(?P<examname>[(A-9)*]+)/addcenter,addcenter,name="addcenter"),
]
