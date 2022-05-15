from django.dispatch import receiver
from django.db.models.signals import post_save,pre_delete

from blog.models import Blog, Post


#заменить на create post
@receiver(post_save, sender=Post)
def save_post(sender, instance,created ,**kwargs):
    if created:
        blog = Blog.objects.filter(posts = instance)[0]
        blog.post_count +=1
        blog.save()

@receiver(pre_delete, sender=Post)
def pre_delete_post(sender, instance ,**kwargs):
    blog = Blog.objects.filter(posts = instance)[0]
    blog.post_count -=1
    blog.save()