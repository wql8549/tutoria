# -*- coding: utf-8 -*-
from django.contrib.auth.models import User, Group
from tpsp_bs.models import t_user,t_task,reslist
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class T_userSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = t_user
        fields=('username','email')
class T_taskSerializer(serializers.HyperlinkedModelSerializer):
    task_email = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='email'
     )
    class Meta:
        model = t_task
        fields=('id','t_taskname','resnum','task_email','creatdate')

class ReslistSerializer(serializers.HyperlinkedModelSerializer):
    taskid = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='id'
     )
    class Meta:
        model = reslist
        fields=('id','taskid','fileurl','creatdate','update')

