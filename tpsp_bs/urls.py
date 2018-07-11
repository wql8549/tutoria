from django.conf.urls import *
from tpsp_bs import views
import tutoria.settings
# from .views import  UserInfoUpdate
from webserver.views import login
from django.contrib.auth import views as user_views
from django.views.static import serve

urlpatterns = [
    url(r'^$', views.login),
    url(r'^login/$',views.login),
    url(r'^index/$',views.index),
    url(r'^logout/$',views.logout),
    url(r'^user/list/$', views.userList, name='user_list'),
    url(r'^user/list/(.+)/$',views.userList,name='user_listcc'),
url(r'^user/$',views.userList),
url(r'^user/add/$',views.userAdd),
url(r'^user/alter/(.+)/$',views.userAlter,name='user_alter'),
url(r'^cmdb/serverlist/$',views.tasklist, name='server_list'),
url(r'^cmdb/serverlist/(.+)/$',views.tasklist,name='server_listcc'),
url(r'^cmdb/serveradd/$',views.taskAdd,name='tpsp_add'),

  #  url(r'^cmdb/serveradd/$',views.serverAdd, name='server_add'),

]

