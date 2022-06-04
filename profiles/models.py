from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model


User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    about_me = models.TextField(
        verbose_name=_("About me"), default="Say something about yourself"
    )
    profile_photo = models.ImageField(
        verbose_name=_("Profile photo"), default="/profile_default.png"
    )

    def __str__(self):
        return f"{self.user.username}'s profile"