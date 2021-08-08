from django.contrib import admin
from booktest.models import BookInfo
from booktest.models import HeroInfo


# Register your models here.

# 创建admin管理类显示
class BookInfoAdmin(admin.ModelAdmin):
    """图书模型管理类"""
    # 配置后再BOOK INFO中显示id、btitle、bpub_date字段
    list_display = ['id', 'btitle', 'bpub_date']


class HeroInfoAdmin(admin.ModelAdmin):
    """英雄模型管理类"""
    list_display = ['id', 'hname', 'hcomment', 'hbook']


admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)