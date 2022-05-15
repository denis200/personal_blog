import factory
from factory.django import DjangoModelFactory
from mixer.backend.django import mixer

from users.models import User


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = 'Denis'
    email = 'soundze@mail.ru'
    password = factory.PostGenerationMethodCall('set_password',
                                            'Password2022')
    is_superuser = True
    is_staff = True