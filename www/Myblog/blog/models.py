from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    """分类"""

    STATUS_ITEMS = (
        (1,"正常"),
        (0, "删除"),
    )
    name = models.CharField(max_length=50, verbose_name="名称")
    status = models.IntegerField(choices=STATUS_ITEMS, default=1, verbose_name="状态")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="作者")
    is_nav = models.BooleanField(default=False, verbose_name="是否为导航")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '分类'
        verbose_name = verbose_name_plural

class Tag(models.Model):
    """标签"""
    STATUS_ITEMS = (
        (1,"正常"),
        (0, "删除"),
    )
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="作者")
    status = models.IntegerField(choices=STATUS_ITEMS, default=1, verbose_name="状态")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural ='标签'

class Post(models.Model):
    """文章"""
    STATUS_ITEMS = (
        (0, "删除"),
        (1, "正常"),
        (2, "草稿")
        
    )
    title = models.CharField(max_length=255, verbose_name="标题")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="作者")
    category = models.ForeignKey(Category, verbose_name="分类", on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, verbose_name="标签")
    desc = models.CharField(max_length=1024, verbose_name="摘要")
    content = models.TextField(verbose_name="正文")
    status = models.IntegerField(choices=STATUS_ITEMS, default=2, verbose_name="状态")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = verbose_name_plural ='文章'

