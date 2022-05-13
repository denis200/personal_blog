from django.db import models
from users.models import User

class Blog(models.Model):
    user = models.OneToOneField(User)
    post_count = models.PositiveIntegerField(verbose_name="Количество постов")


class Post(models.Model):
    blog = models.ForeignKey(Blog,verbose_name="Запись блога",related_name='posts',on_delete = models.CASCADE)
    title = models.CharField(verbose_name="Заголовок",blank = False)
    text = models.CharField(verbose_name="Текст",max_length=140)
    created = models.DateTimeField(auto_now=True)
    read = models.BooleanField(default = False)