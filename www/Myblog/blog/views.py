from django.shortcuts import render
from .models import Category, Post

# from .models import Blog
# # Create your views here.


# def index(request):
#     blogs = Blog.objects.all().order_by("-create_time")  # 查询所有文章

#     return render(request, "index.html",
#     {"blogs":blogs}
#     )

# def read_blog(request, id):
#     print(f"{id}:我是通过点击前端链接来的")
#     blog = Blog.objects.get(id=id)
#     return render(request, "content.html", {"blog":blog})

from django.db.models import Q

categories = None

def index(request):
    global categories
    categories = Category.objects.filter(is_nav=True, status=1) # Q(is_nav=True)|Q(status=1)
    blogs = Post.objects.filter(status=1)
    for blog in blogs:
        print(blog.tags.all())
    return render(request, "index.html",
    {
        "categories":categories,
        "blogs":blogs
    }
    ) 

def detail(request, id):
    blog = Post.objects.get(id=id)
    return render(request, "detail.html",
    {
        "categories":categories,
        "blog":blog
    }
    ) 

def get_posts_by_category(request, id):
    blogs = Post.objects.filter(status=1, category_id = id)
    print(blogs)
    for blog in blogs:
        print(blog.tags.all())
    return render(request, "index.html",
    {
        "categories":categories,
        "blogs":blogs
    }
    ) 