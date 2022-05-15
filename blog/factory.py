import factory
from factory.django import DjangoModelFactory
from mixer.backend.django import mixer

from users.models import User


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("first_name")
    email = factory.Faker('email')
    password = factory.PostGenerationMethodCall('set_password',
                                            'Password2022')
