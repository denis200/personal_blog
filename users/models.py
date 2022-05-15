from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.dispatch import receiver
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save

from blog.models import Blog

from .managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(verbose_name=_("Username"), max_length=255, unique=True)
    email = models.EmailField(verbose_name=_("Email Address"), unique=True)
    date_joined = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username",]

    objects = CustomUserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.username


class UserFollowing(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.DO_NOTHING, related_name="following")
    following_user_id = models.ForeignKey(User,on_delete=models.DO_NOTHING, related_name="followers")
    created = models.DateTimeField(auto_now_add=True)


@receiver(post_save, sender=User)
def save_user(sender, instance,created ,**kwargs):
    if created:
        Blog.objects.create(user = instance)