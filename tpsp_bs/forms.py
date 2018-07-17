# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User

class UserForm(forms.Form):
    username = forms.CharField(label='',max_length=100,widget=forms.TextInput(
        attrs={'id': 'username','placeholder': 'User'}))
    password = forms.CharField(label='',widget=forms.PasswordInput(
        attrs={'id': 'password','placeholder': 'Password'}))

class RegisterForm(forms.Form):
    isactive = [
        (0, '禁用'),
        (1, '启用'),
    ]
    add_user = forms.CharField(label='add_user',max_length=20,widget=forms.TextInput(
        attrs={'id': 'add_user', 'name': 'add_user','placeholder': '请输入用户名'}))
    add_password = forms.CharField(label='add_password',max_length=20,widget=forms.PasswordInput(
        attrs={'id': 'add_password','name': 'add_password', 'placeholder': '请输入密码'}))
    add_passwordtwo = forms.CharField(label='add_passwordtwo',max_length=20,widget=forms.TextInput(
        attrs={'id': 'add_passwordtwo','name': 'add_passwordtwo', 'placeholder': '请确认密码'}))
    add_email = forms.EmailField(label='add_email',max_length=20,widget=forms.TextInput(
        attrs={'id': 'add_email', 'name': 'add_email','placeholder': '请输入您的邮箱'}))
    add_isactive = forms.IntegerField(widget=forms.Select(choices=isactive))

class AlterForm(forms.Form):
    isactive = [
        (0, '禁用'),
        (1, '启用'),
    ]
    alter_email = forms.EmailField(label='add_email', max_length=20,initial='class', widget=forms.TextInput(
        attrs={'id': 'add_email', 'name': 'add_email', 'placeholder': '请输入您的邮箱'}))
    alter_isactive = forms.IntegerField(widget=forms.Select(choices=isactive))
class T_taskForm(forms.Form):

    taskid=forms.IntegerField()
    t_taskname=forms.CharField(label='taskname',max_length=40)
    task_email=forms.ModelMultipleChoiceField(queryset=User.objects.all())
class plugForm(forms.Form):
    ptclist = [(1, u'配置'), (2, u'文件')]
    tpsp_taskid=forms.IntegerField()
    name=forms.CharField(max_length=50)
    platform_id=forms.IntegerField(widget=forms.Select(choices=ptclist))
    version=forms.IntegerField()
    description=forms.CharField(max_length=50)
class plug_fileForm(forms.Form):
    ftypelist=((2,'文件'),)
    pluginid=forms.IntegerField(label='插件id')
    name=forms.CharField(label='文件名称',max_length=40)
    ftype=forms.IntegerField(label='类型',widget=forms.Select(choices=ftypelist))
    fpath=forms.FileField(label='文件地址')
    version=forms.CharField(label='插件版本',max_length=20)

class plug_configForm(forms.Form):
    ftypelist=((1,'配置'),)
    pluginid=forms.IntegerField()
    name=forms.CharField(max_length=40)
    ftype=forms.IntegerField(label='类型',widget=forms.Select(choices=ftypelist))
    fpath=forms.URLField()
    version=forms.CharField(max_length=20)



