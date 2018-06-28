# -*- coding: utf-8 -*-
from django.contrib.auth.models import User, Group
from tpsp_bs.models import t_user
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