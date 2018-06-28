# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.decorators import api_view,schema
from rest_framework.schemas import AutoSchema
from quickstart.serializers import UserSerializer, GroupSerializer,T_userSerializer
from tpsp_bs.models import t_user
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt



class UserViewSet(viewsets.ModelViewSet):
    """
    API端：允许查看和编辑用户
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API端：允许查看和编辑组
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer



class T_userViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API端：允许查看
    """
    queryset = t_user.objects.all()
    serializer_class = T_userSerializer



@api_view()
def hello_world(request):
    return JsonResponse({"message": "Hello, world!"})
