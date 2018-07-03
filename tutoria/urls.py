# -*- coding: utf-8 -*-
"""tutoria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from rest_framework import routers
from quickstart import views
from django.contrib import admin
from tpsp_bs import views as tviews

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r't_user', views.T_userViewSet)
router.register(r't_task', views.T_taskViewSet)
#router.register(r'purchases/(?P<username>.+)/$', views.ReslistViewSet)




# 使用自动化URL路由，转配我们的API.
# 如有额外需要, 我也为可视化API添加了登陆URLs.
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'test',views.hello_world),
    url(r'hellojq$',tviews.hellojq),
url(r'hellojq1',tviews.hellojq1),
url(r'hellojq2',tviews.hellojq2),
url(r'^purchases/(?P<username>\d+)/$', views.ReslistViewSet),
url(r'^', include(router.urls)),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]