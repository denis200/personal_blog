from django.contrib import admin

from blog.models import Blog, Post


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display =('id','user','post_count')



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display =('id','title','text','created')