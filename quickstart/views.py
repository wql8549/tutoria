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
    date=[
    {
        "Id": 1,
        "Title": "JAVA LOGIC",
        "Author": "Oracle",
        "Price": 10.99,
        "PubDate": "2010-01-01",
        "Category": {
            "Id": 1,
            "Name": "计算机类"
        }
    },
    {
        "Id": 2,
        "Title": "HTML",
        "Author": "W3C",
        "Price": 20.99,
        "PubDate": "2010-02-01",
        "Category": {
            "Id": 1,
            "Name": "计算机类"
        }
    },
    {
        "Id": 3,
        "Title": "SQL BASIC",
        "Author": "Microsoft",
        "Price": 30.99,
        "PubDate": "2010-03-01",
        "Category": {
            "Id": 1,
            "Name": "计算机类"
        }
    },
    {
        "Id": 4,
        "Title": "C# LOGIC",
        "Author": "Microsoft",
        "Price": 40.99,
        "PubDate": "2010-04-01",
        "Category": {
            "Id": 1,
            "Name": "计算机类"
        }
    },
    {
        "Id": 5,
        "Title": "JAVA OOP",
        "Author": "Oracle",
        "Price": 50.99,
        "PubDate": "2010-05-01",
        "Category": {
            "Id": 1,
            "Name": "计算机类"
        }
    },
    {
        "Id": 6,
        "Title": "JAVASCRIPT",
        "Author": "W3C",
        "Price": 10.99,
        "PubDate": "2010-01-01",
        "Category": {
            "Id": 1,
            "Name": "计算机类"
        }
    },
    {
        "Id": 7,
        "Title": "JSP",
        "Author": "Oracle",
        "Price": 20.99,
        "PubDate": "2010-02-01",
        "Category": {
            "Id": 1,
            "Name": "计算机类"
        }
    },
    {
        "Id": 8,
        "Title": "SQL ADVANCE",
        "Author": "Microsoft",
        "Price": 30.99,
        "PubDate": "2010-03-01",
        "Category": {
            "Id": 1,
            "Name": "计算机类"
        }
    },
    {
        "Id": 9,
        "Title": "C# OOP",
        "Author": "Microsoft",
        "Price": 40.99,
        "PubDate": "2010-04-01",
        "Category": {
            "Id": 1,
            "Name": "计算机类"
        }
    },
    {
        "Id": 10,
        "Title": "NTIER",
        "Author": "Microsoft",
        "Price": 50.99,
        "PubDate": "2010-05-01",
        "Category": {
            "Id": 1,
            "Name": "计算机类"
        }
    },
    {
        "Id": 11,
        "Title": "ASP.NET",
        "Author": "Microsoft",
        "Price": 10.99,
        "PubDate": "2010-01-01",
        "Category": {
            "Id": 1,
            "Name": "计算机类"
        }
    },
    {
        "Id": 12,
        "Title": "AJAX",
        "Author": "Microsoft",
        "Price": 20.99,
        "PubDate": "2010-02-01",
        "Category": {
            "Id": 1,
            "Name": "计算机类"
        }
    },
    {
        "Id": 13,
        "Title": "HIBERNATE",
        "Author": "Oracle",
        "Price": 30.99,
        "PubDate": "2010-03-01",
        "Category": {
            "Id": 1,
            "Name": "计算机类"
        }
    },
    {
        "Id": 14,
        "Title": "STRUTS",
        "Author": "Oracle",
        "Price": 40.99,
        "PubDate": "2010-04-01",
        "Category": {
            "Id": 1,
            "Name": "计算机类"
        }
    },
    {
        "Id": 15,
        "Title": "SPRING",
        "Author": "Oracle",
        "Price": 50.99,
        "PubDate": "2010-05-01",
        "Category": {
            "Id": 1,
            "Name": "计算机类"
        }
    },
    {
        "Id": 16,
        "Title": "西游记",
        "Author": "吴承恩",
        "Price": 10.99,
        "PubDate": "2010-01-01",
        "Category": {
            "Id": 2,
            "Name": "文学类"
        }
    },
    {
        "Id": 17,
        "Title": "三国演义",
        "Author": "罗贯中",
        "Price": 20.99,
        "PubDate": "2010-02-01",
        "Category": {
            "Id": 2,
            "Name": "文学类"
        }
    },
    {
        "Id": 18,
        "Title": "水浒传",
        "Author": "施耐庵",
        "Price": 30.99,
        "PubDate": "2010-03-01",
        "Category": {
            "Id": 2,
            "Name": "文学类"
        }
    },
    {
        "Id": 19,
        "Title": "红楼梦",
        "Author": "曹雪芹",
        "Price": 40.99,
        "PubDate": "2010-04-01",
        "Category": {
            "Id": 2,
            "Name": "文学类"
        }
    },
    {
        "Id": 20,
        "Title": "傲慢与偏见",
        "Author": "简奥斯汀",
        "Price": 10.99,
        "PubDate": "2010-01-01",
        "Category": {
            "Id": 2,
            "Name": "文学类"
        }
    },
    {
        "Id": 21,
        "Title": "呼啸山庄",
        "Author": "艾米莉勃朗特",
        "Price": 20.99,
        "PubDate": "2010-02-01",
        "Category": {
            "Id": 2,
            "Name": "文学类"
        }
    },
    {
        "Id": 22,
        "Title": "战争与和平",
        "Author": "列夫托尔斯泰",
        "Price": 30.99,
        "PubDate": "2010-03-01",
        "Category": {
            "Id": 2,
            "Name": "文学类"
        }
    },
    {
        "Id": 23,
        "Title": "红与黑",
        "Author": "司汤达",
        "Price": 40.99,
        "PubDate": "2010-04-01",
        "Category": {
            "Id": 2,
            "Name": "文学类"
        }
    },
    {
        "Id": 24,
        "Title": "灰姑娘",
        "Author": "格林",
        "Price": 10.99,
        "PubDate": "2010-01-01",
        "Category": {
            "Id": 3,
            "Name": "儿童类"
        }
    },
    {
        "Id": 25,
        "Title": "卖火柴的小女孩",
        "Author": "格林",
        "Price": 20.99,
        "PubDate": "2010-02-01",
        "Category": {
            "Id": 3,
            "Name": "儿童类"
        }
    },
    {
        "Id": 26,
        "Title": "白雪公主",
        "Author": "格林",
        "Price": 30.99,
        "PubDate": "2010-03-01",
        "Category": {
            "Id": 3,
            "Name": "儿童类"
        }
    },
    {
        "Id": 27,
        "Title": "睡美人",
        "Author": "格林",
        "Price": 40.99,
        "PubDate": "2010-04-01",
        "Category": {
            "Id": 3,
            "Name": "儿童类"
        }
    },
    {
        "Id": 28,
        "Title": "小红帽",
        "Author": "安徒生",
        "Price": 10.99,
        "PubDate": "2010-05-01",
        "Category": {
            "Id": 3,
            "Name": "儿童类"
        }
    },
    {
        "Id": 29,
        "Title": "拇指姑娘",
        "Author": "安徒生",
        "Price": 20.99,
        "PubDate": "2010-06-01",
        "Category": {
            "Id": 3,
            "Name": "儿童类"
        }
    },
    {
        "Id": 30,
        "Title": "青蛙王子",
        "Author": "安徒生",
        "Price": 30.99,
        "PubDate": "2010-07-01",
        "Category": {
            "Id": 3,
            "Name": "儿童类"
        }
    },
    {
        "Id": 31,
        "Title": "海的女儿",
        "Author": "安徒生",
        "Price": 40.99,
        "PubDate": "2010-08-01",
        "Category": {
            "Id": 3,
            "Name": "儿童类"
        }
    }
]
    print 'HttpResponse',type(date)
    return HttpResponse(date)
