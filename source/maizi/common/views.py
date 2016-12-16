#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2015/11/3
@author: wuzongjian
Common模块View业务处理。
"""

from django.shortcuts import render,HttpResponse
from common.models import *
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import  PageNotAnInteger,Paginator,InvalidPage,EmptyPage
import json


def global_setting(request):
    # 有情连接
    link_list = Links.objects.all()
    link_pic = Links.objects.filter(is_pic=True)
    reads_list_AV = RecommendedReading.objects.filter(reading_type='AV')[0:3]  # 取出三条
    reads_list_DC = RecommendedReading.objects.filter(reading_type='DC')[0:3]  # 取出三条
    reads_list_NW = RecommendedReading.objects.filter(reading_type='NW')[0:3]  #
    # 搜索关键字
    keyword_list = Keywords.objects.all()
    #职业课程
    CareerCourseList = CareerCourse.objects.all().order_by('id')[0:10]
    teacher_list = UserProfile.objects.filter(is_staff = '1')[2:16]
    media_url = settings.MEDIA_URL
    return locals()

# keywords_search
@csrf_exempt
def keywords_search(request):
    word = request.GET.get("value")
    print(word)
    try:
        if word != '':
            word_list =[w.name for w in Keywords.objects.filter(name__icontains= word)] #这句话超长。
            return  HttpResponse (json.dumps(word_list),content_type="appliction/josn")
    except Exception as e:
        print(e)


# 首页
def index(request):
    try:
        career_list = CareerCourse.objects.all()#默认排例是按加入的id 降序排。最新的排在最前面。
        career_list = getPage(request,career_list)
        Ad_list = Ad.objects.all()
        hot_career_list = CareerCourse.objects.all().order_by('-student_count')
        hot_career_list = getPage(request, hot_career_list)

        most_career_list = CareerCourse.objects.all().order_by('-click_count')
        most_career_list = getPage(request, most_career_list)

    except Exception as e:
        print(e)
    return render(request, "common/index.html", locals())




#测试
def aaa(request):
    return render(request,"common/base.html", locals())

#分页
def getPage(request,paginator_list):
    paginator = Paginator(paginator_list, 8)
    page = request.GET.get('page')
    try:
        paginator_list = paginator.page(page)
    except PageNotAnInteger:
        paginator_list = paginator.page(1)
    except EmptyPage:
        paginator_list = paginator.page(paginator.num_pages)
    return paginator_list

def login(request):
    return render(request,'common/login.html',locals())

#教师展示详细页
def teacher(request):
    try:
        name = request.GET.get("center")
        print(name)
        if name != '':
            teacher_info = UserProfile.objects.filter(username = name).values()[0]
            print(teacher_info)
            # teahcer_info 返回的是字典，.get这里是字典的操作看里面是否有'id'
            course = Course.objects.filter(teacher= teacher_info.get('id'))
            print([cou.name for cou in course])
    except Exception as e:
        print(e)
    return render(request,'common/teachershow.html',locals())