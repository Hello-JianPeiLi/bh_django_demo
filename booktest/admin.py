from django.contrib import admin
from booktest.models import BookInfo
from booktest.models import HeroInfo
from booktest.models import PicTest
from booktest.models import AreaInfo


# Register your models here.

# 创建admin管理类显示
class BookInfoAdmin(admin.ModelAdmin):
    """图书模型管理类"""
    # 配置后再BOOK INFO中显示id、btitle、bpub_date字段
    list_display = ['id', 'btitle', 'bpub_date']


class HeroInfoAdmin(admin.ModelAdmin):
    """英雄模型管理类"""
    list_display = ['id', 'hname', 'hcomment', 'hbook']


class PicTestAdmin(admin.ModelAdmin):
    list_display = ['id', 'pic_name', 'pic_path']


class AreaStackedInline(admin.StackedInline):
    """关联对象---以块的形式嵌入"""
    model = AreaInfo
    extra = 2


class AreaTabularInline(admin.TabularInline):
    """关联对象---以表格的形式嵌入"""
    model = AreaInfo
    extra = 2


class AreaInfoAdmin(admin.ModelAdmin):
    list_per_page = 10
    # actions_on_top = False
    # list_display 可以添加字段，也可以添加方法如下，title，parent就是model中的方法
    list_display = ['id', 'atitle', 'title', 'parent']
    # 右侧栏过滤器
    list_filter = ['atitle']
    # 搜索框
    search_fields = ['id', 'atitle']
    # 编辑页面显示字段顺序
    # fields = ['aParent', 'atitle']
    # 分组显示 不能和上面 fields 共同存在
    fieldsets = (
        ('基本', {'fields': ['atitle']}),
        ('高级', {'fields': ['aParent']})
    )
    # 以块的形式嵌入
    # inlines = [AreaStackedInline]
    # 以表格的形式嵌入
    inlines = [AreaTabularInline]


admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)
admin.site.register(PicTest, PicTestAdmin)
admin.site.register(AreaInfo, AreaInfoAdmin)
