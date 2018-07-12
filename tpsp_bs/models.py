# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import django.utils.timezone as timezone
from django.db import models
import time
from django.contrib.auth.models import User

# Create your models here.
#tpsp管理后台正式模型
class platforminfo(models.Model):
    id=models.AutoField()
    platformname=models.CharField(max_length=40,null=True,blank=True);
    puturl=models.URLField();

class netbars(models.Model):

    gid=models.IntegerField()
    name=models.CharField(max_length=50)
    platformid=models.ForeignKey(platforminfo)
    creatdate=models.DateField(auto_created=True)

class plugin_base(models.Model):
    id=models.AutoField()
    platform_id=models.ForeignKey(platforminfo)
    tpsp_taskid=models.IntegerField()
    name=models.CharField(max_length=50)
    description=models.TextField(256)
    user_id=models.ForeignKey(User)
    created_at=models.DateField(auto_created=True,default=timezone.now)
    updated_at=models.DateField()
    deleted_at=models.DateField()
    class Meta:
        abstract=True
class plugin_templation(plugin_base):
    id=models.AutoField()
    plugin_config=models.TextField(max_length=256)
class plusins(plugin_base):
    id=models.AutoField()
    version=models.CharField()
    


class t_netbar(models.Model):

    gid=models.IntegerField()
    creatdate=models.DateField(auto_created=True)

class t_user(models.Model):
    ue_list=((0,'无'),(1,'默认发件人'),(2,'默认收件人'),(3,'发件人'),(4,'收件人'))
    username=models.CharField(max_length=20,verbose_name='用户名')
    password=models.CharField(max_length=50)
    user_email=models.IntegerField(default=0,choices=ue_list,verbose_name='邮件关联') #0 非默认邮件，1、默认邮件发送，2、默认邮件收件人，3、默认邮件抄送人
    email=models.EmailField('email',blank=True,null=True)
    def __str__(self):
        return self.username

class t_task(models.Model):
    t_taskname=models.CharField(max_length=40)
    resnum=models.IntegerField() #对应res数量，保持一致
    task_email=models.ManyToManyField(User)#任务关联收件人
    creatdate=models.DateField(default=timezone.now,null=True,blank=True)
    def __str__(self):
        return str(self.id)


def get_file_path(instance, filename):
        print instance
        print instance.id
        print instance.taskid
        print 'task_{0}/res_{1}_{2}_{3}' .format(instance.taskid,instance.id,int(time.time()),filename)
        return 'task_{0}/res_{1}_{2}_{3}'.format(instance.taskid,instance.id,int(time.time()),filename)
class reslist(models.Model):
    taskid=models.ForeignKey(t_task)
    fileurl=models.FileField(upload_to=get_file_path,null=True,blank=True)
    creatdate=models.DateTimeField(default=timezone.now,null=True,blank=True)
    update=models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.id)

    class Meta:
        unique_together = ('taskid', 'creatdate')
        ordering = ['creatdate']


class t_taskput(models.Model):
    state_list=((0,'发布中'),(1,'remove'))
    t_taskputname=models.CharField(max_length=40)
    t_taskid=models.ManyToManyField(t_task)
    t_reslistput=models.CharField(max_length=32)#md5(t_taskid+''.jion([reslist.update]))
    state=models.IntegerField(choices=state_list,default=0)
    git=models.ManyToManyField(t_netbar)
    creatdate=models.DateTimeField(auto_now=True)
    update=models.DateTimeField(auto_now=True)