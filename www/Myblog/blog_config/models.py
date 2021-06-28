from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Link(models.Model):
    """友情链接"""
    STATUS_ITEMS = (
        (1,"正常"),
        (0, "删除"),
    )
    title = models.CharField(max_length=50, verbose_name="网站名称")
    href = models.URLField(verbose_name="链接")
    status = models.IntegerField(choices=STATUS_ITEMS, default=1, verbose_name="状态")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="作者")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    weight = models.IntegerField(choices=zip(range(1,11), range(1,11)),default=1, verbose_name="权重")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = verbose_name_plural ='友情链接'

class SideBar(models.Model):
    """侧边栏"""
    TYPE_ITEMS = (
        (1,"HTML"),
        (2, "最新文章"),
        (3, "最热文章"),
        (4, "最近评论"),
    )
    STATUS_ITEMS = (
        (1,"展示"),
        (0, "隐藏"),
    )
    title = models.CharField(max_length=50, verbose_name="标题")
    display_type = models.IntegerField(choices=TYPE_ITEMS, default=1, verbose_name="展示类型")
    status = models.IntegerField(choices=STATUS_ITEMS, default=1, verbose_name="状态")
    content = models.CharField(max_length=500, verbose_name="内容")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="作者")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = verbose_name_plural ='侧边栏'