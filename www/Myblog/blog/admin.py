from django.contrib import admin

from .models import Category, Tag, Post
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'owner', 'is_nav', 'post_count','created_time')
    fields = ('name', 'status',  'is_nav')

    # select * from Post p where p.category = 'Demo'
    def post_count(self, obj):
        return f"{obj.post_set.count()}篇文章"
        
    post_count.short_description = "文章数"

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        print(request.user)
        return super(CategoryAdmin, self).save_model(request, obj, form, change)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('category','title', 'owner', 'status')
    exclude =('owner',)

    actions_on_top = True # 首页的按钮
    actions_on_bottom = True # 首页的按钮

    save_on_top = True # 编辑页面的按钮
    search_fields = ('title','category__name')

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        print(request.user)
        return super(PostAdmin, self).save_model(request, obj, form, change)
    