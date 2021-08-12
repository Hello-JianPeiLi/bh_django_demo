from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import HttpResponseRedirect
from django.http import JsonResponse
from booktest.models import BookInfo
from booktest.models import HeroInfo
from booktest.models import AreaInfo
from datetime import date
import json


# Create your views here.

def index(request):
    books = BookInfo.objects.all()
    for book in books:
        print(book.id)
    return render(request, 'booktest/index.html', {"books": books})


def create(request):
    book = BookInfo()
    book.btitle = '流星蝴蝶剑'
    book.bpub_date = date(1990, 6, 6)
    book.save()
    # return HttpResponse('ok')
    return HttpResponseRedirect('/index')


def remove(request, bid):
    print("=>=>=>=>=>=>=>", bid)
    book = BookInfo.objects.filter(id=bid)
    book.delete()
    return HttpResponseRedirect('/index')


def detail(request, bid):
    book = BookInfo(id=bid)
    heros = book.heroinfo_set.all()
    return render(request, 'booktest/detail.html', {"heros": heros})


def area(request):
    area = AreaInfo.objects.get(atitle='广州市')
    print(area.atitle)
    parent = area.aParent
    children = area.areainfo_set.all()
    return render(request, 'booktest/area.html', {"area": area, "parent": parent, "children": children})


def login(request):
    return render(request, 'booktest/login.html', {})


def check(request):
    print(request.META['REMOTE_ADDR'])
    username = request.POST.get('username')
    passwrod = request.POST.get('password')
    print(username, "---", passwrod)
    json_data = {"username": username, "password": passwrod}
    # print(type(json_data))
    return HttpResponse("pok")
    # return HttpResponse(username, passwrod)


def block_ip(func):
    def wrapper(request, *args, **kwargs):
        ip_list = ['127.0.0.1']
        if request.META['REMOTE_ADDR'] in ip_list:
            return HttpResponse('<h1>你这个ip不给访问</h1>')
        else:
            return func(request, *args, **kwargs)

    return wrapper


# @block_ip
def login_ajax(request):
    # ajax 使用application/json 则使用body获取数据
    print(request.META['REMOTE_ADDR'])
    body = json.loads(request.body.decode('utf-8'))
    username = body.get('username')
    password = body.get('password')
    # if username != 'libai' and password == '123':
    # return JsonResponse({'msg': '登录成功', 'code': '1'})
    return HttpResponse('pl')
