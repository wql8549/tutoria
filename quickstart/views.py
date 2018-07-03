# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.decorators import api_view,schema
from rest_framework.schemas import AutoSchema
from quickstart.serializers import UserSerializer, GroupSerializer,T_userSerializer,T_taskSerializer,ReslistSerializer
from tpsp_bs.models import t_user,t_task,reslist
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import action




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
class T_taskViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API端：允许查看
    """
    queryset = t_task.objects.all()

    serializer_class = T_taskSerializer

class ReslistViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API端：允许查看
    """
    queryset = reslist.objects.all()
    serializer_class = ReslistSerializer

    @action(detail=True)
    def taskid(self, request):
        taskid=request.data
        print taskid




@api_view()
def hello_world(request):
    return HttpResponse([{"message": "Hello, world!liuxwindowtest2","message2": "Hello, world!liuxwindowtest2"}])
