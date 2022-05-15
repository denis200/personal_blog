from django.db import transaction
from django.core.management.base import BaseCommand
from mixer.backend.django import mixer

from blog.models import Blog, Post
from users.models import User, UserFollowing


class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [UserFollowing,Blog,User,Post]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")
        admin = mixer.blend('users.User',username = 'Admin',email = 'admin@mail.ru',is_superuser = True,is_staff = True)
        admin.set_password('Password2022')
        admin.save()

        mixer.cycle(10000).blend('users.User')
        blogs = Blog.objects.all().exclude(user_id = admin.id )
        mixer.cycle(10000).blend('blog.Post',blog = mixer.sequence(*blogs))
        mixer.cycle(10000).blend('users.UserFollowing',blog = mixer.sequence(*blogs),following_user_id = admin)
        