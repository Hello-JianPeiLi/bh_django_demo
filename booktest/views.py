from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import HttpResponseRedirect
from booktest.models import BookInfo
from booktest.models import HeroInfo
from booktest.models import AreaInfo
from datetime import date


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
