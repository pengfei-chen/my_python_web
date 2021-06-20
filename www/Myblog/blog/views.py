from django.shortcuts import render

from .models import Blog
# Create your views here.


def index(request):
    blogs = Blog.objects.all().order_by("-create_time")  # 查询所有文章

    return render(request, "index.html",
    {"blogs":blogs}
    )

def read_blog(request, id):
    print(f"{id}:我是通过点击前端链接来的")
    blog = Blog.objects.get(id=id)
    return render(request, "content.html", {"blog":blog})
