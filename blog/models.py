from django.db import models


class Blog(models.Model):
    """ Модель блога пользователя """
    user = models.OneToOneField(to='users.User', on_delete=models.CASCADE)
    post_count = models.PositiveIntegerField(verbose_name="Post count",default=0)

    def __str__(self):
        return f"{self.user.username}'s blog"


class Post(models.Model):
    """ Модель поста блога"""
    blog = models.ForeignKey(Blog,verbose_name="Blogs owner",related_name='posts',on_delete = models.CASCADE)
    title = models.CharField(verbose_name="Title",blank = False,max_length=140)
    text = models.CharField(verbose_name="Text",max_length=140)
    created = models.DateTimeField()

    def __str__(self):
        return f"Post_id №{self.pk}"


class ViewPost(models.Model):
    """ Модель просмотренных пользователем постов"""
    post = models.ForeignKey(Post,on_delete = models.CASCADE,related_name='views')
    user = models.ForeignKey(to='users.User',on_delete= models.DO_NOTHING,related_name='users')
