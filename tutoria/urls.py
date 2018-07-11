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
from tpsp_bs import views  as tviews
from django.contrib import admin
import tutoria.settings
from django.views.static import serve
admin.autodiscover()
from django.conf.urls import handler404, handler500

handler404 = "webserver.views.page_not_found"
handler500 = "webserver.views.page_error"
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r't_user', views.T_userViewSet)



# 使用自动化URL路由，转配我们的API.
# 如有额外需要, 我也为可视化API添加了登陆URLs.
urlpatterns = [
url(r'^admin/', admin.site.urls),
#url(r'^webserver/', include('webserver.urls')),
url(r'^tpsp_bs/', include('tpsp_bs.urls')),
    #url(r'^login', tviews.login_view, name='login'),
    #url(r'^logout', tviews.logout_view),
    #url(r'^register', tviews.register_view, name='register'),


    url(r'hello/', views.hello_world),

    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]