from django.contrib import admin

from blog.models import Blog, Post, ViewPost


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display =('id','user','post_count')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display =('id','title','text','created')


@admin.register(ViewPost)
class ViewPostAdmin(admin.ModelAdmin):
    list_display =('id','post','user')