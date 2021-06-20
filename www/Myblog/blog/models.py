from django.db import models

# Create your models here.

class Blog(models.Model):
    # title = models.TextField(max_length=50)
    title = models.CharField(max_length=50, verbose_name="标题")
    content = models.TextField(verbose_name="文章内容", default="")
    count = models.IntegerField(verbose_name="阅读次数", default=0)
    create_time = models.DateTimeField(auto_now=True, verbose_name="创建时间")

    class Meta:
        verbose_name = '博客管理'
        verbose_name_plural = verbose_name

    def __str__(self) -> str:
        return self.title