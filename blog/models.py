from django.db import models
from users.models import User

class Blog(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    post_count = models.PositiveIntegerField(verbose_name="Количество постов")


class Post(models.Model):
    blog = models.ForeignKey(Blog,verbose_name="Пренадлежит блогу",related_name='posts',on_delete = models.CASCADE)
    title = models.CharField(verbose_name="Заголовок",blank = False,max_length=140)
    text = models.CharField(verbose_name="Текст",max_length=140)
    created = models.DateTimeField(auto_now=True)


class ViewPost(models.Model):
    post = models.ForeignKey(Post,on_delete = models.CASCADE,related_name='views')
    user = models.ForeignKey(User,on_delete= models.DO_NOTHING,related_name='users')