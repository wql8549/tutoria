# -*- coding: utf-8 -*-
from django import forms

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
    