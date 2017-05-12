from django.conf.urls import url,include
from django.contrib import admin
from AuthPortal.views import signup,login_user,logout_user

app_name='APIWebInterface'
urlpatterns = [
    url(r'^admin/', admin.site.urls),
]

# added the login patterns

urlpatterns += [
    url(r'^signup/$', signup, name="signup"),
    url(r'^login/$', login_user, name="login"),
    url(r'^logout/$', logout_user, name="logout"),
]

# added url for examcreation

urlpatterns += [
    url(r'^', include('CRUDPage.urls'), name='crudepage'),
]
