# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import t_user,t_netbar,t_task,t_taskput,reslist
from tutoria.settings import MEDIA_URL,ALLOWED_HOSTS

@admin.register(t_user)
class T_userAdmin(admin.ModelAdmin):
    #设置显示列表地
    list_display = ('id','username','user_email','email')
    #设置每页显示数量
    list_per_page = 20
    #设置默认排序字段，-降序
    ordering = ('id',)
    #list_editable 设置默认可编辑字段
    #list_editable = ['user_email','email']
    #设置可以点击进入字段
    list_display_links = ('id','username')
    list_filter = ('user_email',)
    search_fields =('username', 'email') #搜索字段
    fields = (('username','user_email'),'email')

@admin.register(reslist)
class ReslistAdmin(admin.ModelAdmin):
    list_display = ('taskid','id','fileurl2','creatdate','update')
    list_display_links = ('fileurl2',)
    ordering = ('taskid','id')
    list_filter = ('taskid',)
    exclude = ('creatdate','update')
    search_fields = ('id',)

    def taskid(self,obj):
        return obj.id
    def fileurl2(self,obj):
        return "http://%s%s%s"%(ALLOWED_HOSTS[0],MEDIA_URL,obj.fileurl)

class ReslistAdmin(admin.TabularInline):
    model=reslist
    extra=0


@admin.register(t_task)
class T_taskAdmin(admin.ModelAdmin):
    inlines = [ReslistAdmin,]
    list_display = ('id','t_taskname','resnum','email2')
    filter_horizontal = ('task_email',)
    exclude = ('creatdate',)
    def  email2(self,obj):
        '''
        这个方法就是用来对salt_minion_id这个字段做处理，把我们需要展示的前端内容截取出来。需要注意的是，方法名必须要和在list_display里面的一致，这样才可以调用。
        '''

        return [a.email for a in obj.task_email.all()]   # host_target是我们SaltGroup表中多对多的字段，salt_minion_id是刚才我们自定义的字段，
    email2.short_description = "email "     # 对salt_minion_id这个做个简短的title。



@admin.register(t_taskput)
class T_taskputAdmin(admin.ModelAdmin):
    list_display = ('t_taskputname',"t_reslistput",'state','creatdate','update')


admin.site.site_header = 'tpsp管理后台'
admin.site.site_title = 'tpsp管理后台'


admin.site.register(t_netbar)


