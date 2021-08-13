from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import redirect
from django.http import JsonResponse
from booktest.models import BookInfo
from booktest.models import HeroInfo
from booktest.models import AreaInfo
from datetime import date
import json
from test1 import settings
from booktest.models import PicTest
from django.core.paginator import Paginator


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
    parent = area.aParent
    children = area.areainfo_set.all()
    return render(request, 'booktest/area.html',
                  {"area": area, "parent": parent, "children": children})


# /login
def login(request):
    # 获取cookie
    print(request.META['REMOTE_ADDR'])
    print("---", request.META['USERNAME'])
    if 'is_login' in request.session:
        return redirect('/index')
    if 'username' in request.COOKIES:
        # 获取记住的用户名
        username = request.COOKIES['username']
    else:
        username = ''
    return render(request, 'booktest/login.html', {'username': username})


# /check
def check(request):
    print(request.META['REMOTE_ADDR'])
    username = request.POST.get('username')
    password = request.POST.get('password')
    remember = request.POST.get('flag')
    response = redirect('/index')
    if username == 'libai' and password == '123':
        if remember == 'on':
            # 设置cookie有效60s
            response.set_cookie('username', username, max_age=60)
            # 记住用户的登录状态
            request.session['is_login'] = True
        return response
    else:
        return redirect('/login')


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
    response = redirect('/login')
    body = json.loads(request.body.decode('utf-8'))
    usr = body.get('username')
    pwd = body.get('password')
    remember = body.get('flag')
    request.COOKIES['username'] = usr
    if usr == 'libai' and pwd == '123':
        response.set_cookie('username', usr, max_age=30)
        return response
    else:
        return redirect('/login')


def index2(request):
    return render(request, 'booktest/index2.html', {})


def index_login(request):
    if 'is_login' in request.session:
        return redirect('/index')

    if 'username' in request.COOKIES:
        username = request.COOKIES['username']
    else:
        username = ''
    return render(request, 'booktest/index_login.html', {'username': username})


def template_login_check(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    remember = request.POST.get('remember')
    response = redirect('/index')
    if username == 'libai' and password == '123':
        if remember:
            response.set_cookie('username', username, max_age=60)
            request.session['is_login'] = True
            return response
        return response
    else:
        return redirect('/index_login')


def upload_file(request):
    return render(request, 'booktest/upload_file.html', {})


def handle_file(request):
    """上传文件"""
    pic = request.FILES['pic']
    print(pic.name)
    save_path = '%s/booktest/media/%s' % (settings.MEDIA_ROOT, pic)
    print(save_path)
    with open(save_path, 'wb') as f:
        for content in pic.chunks():
            f.write(content)
    PicTest.objects.create(pic='booktest/media/%s' % pic)
    return HttpResponse('ok')


# upload_ajax_file
def upload_ajax_file(request):
    file_obj = request.FILES.get('file')
    pic_name = request.POST.get('pic_name').strip()
    print('file---', file_obj)
    print('pic_name---', pic_name)
    if file_obj is None:
        return JsonResponse({'msg': '请上传图片', 'status': 102})
    if pic_name == '':
        return JsonResponse({'msg': '请输入图片名字', 'status': 103})
    if PicTest.objects.filter(pic_name=pic_name):
        return JsonResponse({'msg': '名字不能重复', 'status': 101})
    save_path = '%s/booktest/media/%s' % (settings.MEDIA_ROOT, file_obj.name)
    with open(save_path, 'wb') as f:
        for content in file_obj.chunks():
            f.write(content)
    PicTest.objects.create(pic_name=pic_name, pic_path='booktest/media/%s' % file_obj.name)
    return JsonResponse({'res': '上传成功', 'status': 100})


def get_pic(request):
    pic_name = request.POST.get('pic_name')
    print(pic_name)
    query_pic = PicTest.objects.get(pic_name=pic_name)
    if not query_pic:
        return JsonResponse({'msg': '没有该图片', 'status': 104})
    get_pic_path = str(query_pic.pic_path)
    ret = {}
    ret["msg"] = '获取图片成功'
    ret["pic_path"] = get_pic_path
    ret["status"] = 105
    print(type(ret))
    print(ret)
    return JsonResponse(ret)


# /get_prov
def get_prov(request):
    areas = AreaInfo.objects.filter(aParent__isnull=True)
    prov_list = list()
    for data in areas:
        prov_list.append((data.id, data.atitle))
    # print(len(prov_list))
    return JsonResponse({'data': prov_list})


# /city/pid
def city(request, pid):
    # area = AreaInfo.objects.get(id=pid)
    # city = area.areainfo_set.all()
    areas = AreaInfo.objects.filter(aParent_id=pid)
    city_list = list()
    for city in areas:
        city_list.append((city.id, city.atitle))
    return JsonResponse({'data': city_list})


# /dis/pid
def dis(request, pid):
    areas = AreaInfo.objects.filter(aParent_id=pid)
    dis_list = list()
    for dis in areas:
        dis_list.append((dis.id, dis.atitle))
    return JsonResponse({'data': dis_list})


def all_area(request):
    areas = AreaInfo.objects.all().order_by('id')
    paginator = Paginator(areas, 10)
    areas = paginator.page(1)
    area_list = list()
    for area in areas:
        area_list.append(area.atitle)
    total = paginator.num_pages
    count = paginator.count
    num = areas.number
    return JsonResponse({'page_total': total, 'data': area_list, 'count': count, 'current': num})
