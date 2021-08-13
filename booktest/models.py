from django.db import models


class BookInfoManager(models.Manager):
    def all(self):
        # 调用父类的all方法，获取所有数据
        books = super().all()
        # 对数据进行过滤
        books = books.filter(isDelete=False)
        # 返回数据
        return books

    def create_book(self, btitle, bpub_date):
        # 获取self所在的模型类
        models_class = self.model
        books = models_class()
        # 上面两句话等价于这句话books = BookInfo()
        # 使用self.model时可以不用关心模型类的类名，自动获取
        books.btitle = btitle
        books.bpub_date = bpub_date
        books.save()
        return books


# Create your models here.
class BookInfo(models.Model):
    """图书类模型"""
    # 书名
    btitle = models.CharField(max_length=20)
    # 出版日期
    bpub_date = models.DateField()
    # 阅读数量
    bread = models.IntegerField(default=0)
    # 评论量
    bcomment = models.IntegerField(default=0)
    # 删除标记
    isDelete = models.BooleanField(default=False)
    #
    objects = BookInfoManager()

    def __str__(self):
        return self.btitle


class HeroInfo(models.Model):
    """英雄信息类"""
    # 英雄名
    hname = models.CharField(max_length=20)
    # 角色性别
    hgender = models.BooleanField(default=False)
    # 评论量
    hcomment = models.CharField(max_length=128)
    # 关联图书
    hbook = models.ForeignKey(BookInfo, on_delete=models.SET_DEFAULT, default='没有书名')
    # 删除标记
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.hname


class AreaInfo(models.Model):
    """地区"""
    # 中文标题
    atitle = models.CharField(verbose_name='地区', max_length=20)
    aParent = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_DEFAULT, default='没有省')

    def title(self):
        return self.atitle

    def parent(self):
        if self.aParent is None:
            return 'null'
        return self.aParent.atitle

    parent.short_descriptions = '父级区域名称'
    title.admin_order_field = 'atitle'
    title.short_description = 'title属性改的地区'

    def __str__(self):
        return self.atitle


class PicTest(models.Model):
    pic_name = models.CharField(max_length=20, default='null', unique=True)
    pic_path = models.ImageField(upload_to='booktest/media')
