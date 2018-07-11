# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

# Create your views here.
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.core.paginator import PageNotAnInteger, Paginator, InvalidPage, EmptyPage
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

import time
import platform
import json

from .forms import UserForm,RegisterForm,AlterForm,T_taskForm
from .models import t_task,reslist
def page_not_found(request):
    '''
    404报错页面
    '''
    return render(request,'404.html')

def page_error(request):
    '''
    500报错页面
    '''
    return render(request,'500.html')

def login(req):
    '''
    登录验证
    '''
    nowtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    if req.method == 'GET':
        uf = UserForm()
        return render(req,'login.html', {'uf': uf,'nowtime': nowtime })
    else:
        uf = UserForm(req.POST)

        if uf.is_valid():
            username = req.POST.get('username', '')
            password = req.POST.get('password', '')
            user = auth.authenticate(username = username,password = password)
            if user is not None and user.is_active:
                auth.login(req,user)
                print 1
                return render(req, 'tpsp_bs_index.html',{'tpspname':req.user.username})
            else:
                print 2
                return render(req, 'login.html', {'uf': uf,'nowtime': nowtime, 'password_is_wrong': '账号或密码错误，重新输入'})
        else:
            print 3
            return render(req, 'login.html', {'uf': uf,'nowtime': nowtime })

@login_required
def index(req):
    system = platform.system()
    if system == 'Windows':
        version = platform.version()
        OsVersion = system + '. '+ version
    else:
        node = platform.node()
        OsVersion = node + '@' + system
    OsVersion='betaV2—'+str(time.time())
    coon={'OsVersion': OsVersion,'tpspname':req.user.username}

    print coon
    return render(req, 'tpsp_bs_index.html', coon)

@login_required
def logout(req):
    '''
    注销
    '''
    auth.logout(req)
    return HttpResponseRedirect('/tpsp_bs/login/')


def geThostIp(request):
    '''
    获取访问的IP
    '''
    if request.META.has_key('HTTP_X_FORWARDED_FOR'):
        ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.META['REMOTE_ADDR']
    return render(request, 'menu.html', {'hostip':'192.168.1.1' })

@login_required
def userList(req,id = 0):
    '''
    用户列表
    '''
    if id != 1:
        User.objects.filter(id = id).delete()
    users = User.objects.all()  #导入User表
    after_range_num = 2     #当前页前显示2页
    befor_range_num = 2     #当前页后显示2页
    try:    #如果请求的页码少于1或者类型错误，则跳转到第1页
        page = int(req.GET.get("page",1))
        if page < 1:
            page = 1
    except ValueError:
        page = 1
    paginator = Paginator(users,11)   #每页显示11
    try:  # 跳转到请求页面，如果该页不存在或者超过则跳转到尾页
        users_list = paginator.page(page)
    except(EmptyPage, InvalidPage, PageNotAnInteger):
        users_list = paginator.page(paginator.num_pages)
    if page >= after_range_num:
        page_range = paginator.page_range#[page - after_range_num:page + befor_range_num]
    else:
        page_range = paginator.page_range#[0:int(page) + befor_range_num]
    return render(req,'userlist.html',{'user_list':users_list,'page_range': page_range,'tpspname':req.user.username})

@login_required
def userAdd(req):
    '''
    添加用户
    '''
    if req.method == "POST":
        user_add = RegisterForm(req.POST)
        if user_add.is_valid():
            data = user_add.cleaned_data
            print (data)
            add_user = data.get('add_user')
            add_password = data.get('add_password')
            add_email = data.get('add_email', '')
            add_isactive = data.get('add_isactive')
            user = User()
            user.username = add_user
            user.set_password(add_password)
            user.email = add_email
            user.is_active = add_isactive
            user.save()
            return render(req, 'useradd.html', {'add_newuser': add_user,'tpspname':req.user.username})
        else:
            errors = user_add.errors
            return render(req, 'useradd.html',{'add_FormInput': user_add,'errors': errors,'tpspname':req.user.username})
    else:
        user_add = RegisterForm()
    return render(req, 'useradd.html', {'add_FormInput': user_add,'tpspname':req.user.username})
@login_required
def userAlter(req, id):
    '''
    修改用户
    '''
    user_alter = AlterForm(req.POST)
    if req.method == "POST":
        if user_alter.is_valid():
            alter_data = user_alter.cleaned_data
            print(alter_data)
            alter_email = alter_data.get('alter_email')
            alter_isactive = alter_data.get('alter_isactive')
            file=alter_data.get('file')
            alt = User.objects.get(id=id)
            alt.email = alter_email
            alt.is_active = alter_isactive
            alt.save()
            return HttpResponseRedirect('/tpsp_bs/user/list/',{'tpspname':req.user.username})
        else:
            errors = user_alter.errors
            return render(req, 'useralter.html', {'alter_FormInput': user_alter, 'errors': errors,'tpspname':req.user.username})
    else:
        try:
            UpdateUser = User.objects.only('username').get(id=id).username
            old_eamil = User.objects.only('email').get(id=id).email
            old_is_active = User.objects.only('is_active').get(id=id).is_active
            if old_is_active:
                old_is_active = 1
            else:
                old_is_active = 0

            form = AlterForm(
                initial={'alter_email': old_eamil}
            )
            return render(req, 'useralter.html', {'alter_FormInput': form, 'UpdateUser': UpdateUser, 'alter_is_active':old_is_active,'tpspname':req.user.username})
        except:
            post = get_object_or_404(User, id=id)
            form = AlterForm(instance=post)
            return render(req, 'useralter.html', {'form': form,'tpspname':req.user.username})




@login_required
def tasklist(request,id=0):
    """
    获取插件列表
    :param request:
    :param id:
    :return:
    """
    if id !=0:
        t_task.objects.filter(id=id).delete()
    if request.method=='POST':
            print request.POST
            pageSize = request.POST.get('pageSize')  # how manufactoryy items per page
            pageNumber = request.POST.get('pageNumber')
            offset = request.POST.get('offset')  # how many items in total in the DB
            search = request.POST.get('search')
            sort_column = request.POST.get('sort')  # which column need to sort
            order = request.POST.get('order')  # ascending or descending
            if search:  # 判断是否有搜索字
                print 'search',search
                all_records = t_task.objects.filter(id=search, asset_type=search, business_unit=search, idc=search)
            else:
                all_records = t_task.objects.all()   # must be wirte the line code here
            print 'all_records',all_records
            all_records_count = all_records.count()

            if not offset:
                offset = 0
            if not pageSize:
                pageSize = 10  # 默认是每页20行的内容，与前端默认行数一致
            pageinator = Paginator(all_records, pageSize)  # 开始做分页
            page = int(int(offset) / int(pageSize) + 1)
            response_data = {'total': all_records_count, 'rows': []}
            for server_li in pageinator.page(page):
                response_data['rows'].append({
                    "id": server_li.id if server_li.id else "",
                    "taskname": server_li.t_taskname if server_li.t_taskname else "",
                    "resnum": server_li.resnum if server_li.resnum else "",
                    "email":'<br />'.join( [a.email for a in server_li.task_email.all()] if server_li.task_email else ""),
                    "resfile": '<br />'.join(['res'+str(a.id)+': '+str(a.fileurl) for a in reslist.objects.filter(taskid=server_li.id)] if server_li.id else ""),
                    "CPUS":'',# server_li.CPUS if server_li.CPUS else "",
                    "OS":'',#server_li.OS if server_li.OS else "",
                    "virtual1": '',#server_li.virtual1 if server_li.virtual1 else "",
                    "status": '',#server_li.status if server_li.status else "",
                })
                print [str(a.fileurl) for a in reslist.objects.filter(taskid=server_li.id)] if server_li.id else ""
            return HttpResponse(json.dumps(response_data))
    return render(request, 'serverlist.html',{'tpspname':request.user.username})

def taskAdd(req):
    '''
    添加任务
    '''
    if req.method == "POST":
        task_add = T_taskForm(req.POST)
        print 'task_add',task_add,task_add.is_valid()
        if task_add.is_valid():
            data = task_add.cleaned_data
            print 'data',data
            add_taskid = data.get('taskid')
            add_t_taskname = data.get('t_taskname')
            add_task_email = data.get('task_email', '')
            print 'add_task_email', add_task_email
            print 'add_task_email',add_task_email[0]

            task = t_task()

            usera=User.objects.filter(username=add_task_email[0]).values('id')[0]['id']
            print 'usera', usera
            print 'usera',usera
            #task.taskid = add_taskid
            task.resnum=1
            task.t_taskname=add_t_taskname
            task.email = add_task_email
            task.save()
            task.task_email.add(usera)
            return render(req, 'serverlist.html', {'tpspname': req.user.username})
        else:
            errors = task_add.errors
            return render(req, 'taskadd.html',{'add_taskFormInput': task_add,'errors': errors,'tpspname':req.user.username})
    else:
        task_add = T_taskForm()
    return render(req, 'taskadd.html', {'add_taskFormInput': task_add,'tpspname':req.user.username})