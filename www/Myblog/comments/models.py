from django.db import models
from blog.models import Post
# Create your models here.

class Comment(models.Model):
    """评论"""
    target = models.ForeignKey(Post, verbose_name="评论目标", on_delete=models.CASCADE)
    nickname = models.CharField(max_length=50, verbose_name="昵称")
    email = models.EmailField(verbose_name="邮箱")
    website = models.URLField(verbose_name="网站地址")
    content = models.TextField(verbose_name="评论内容")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    def __str__(self):
        return f"{self.target} By {self.nickname}"

    class Meta:
        verbose_name = verbose_name_plural ='评论'
