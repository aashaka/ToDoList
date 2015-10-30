from django.conf.urls import patterns,url
from GetThingsDone import views
from django.views.generic.base import TemplateView

urlpatterns=patterns(
'',
#url(r'^profile/upload/profilepicture/$',views.upload_profile,name='profile'),

#url(r'^profile/complete/$',views.profile_complete,name='profile_complete'),
url(r'^list/$',views.index,name='index'),
url(r'^welcome/$',views.welcome,name='welcome'),
url(r'^logout/$',views.log_out,name='logout'),
url(r'^addToDo/$',views.addToDo,name='addToDo'),
url(r'^delete/$',views.delete,name='delete'),
)