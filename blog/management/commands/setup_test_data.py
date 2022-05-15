import random

from django.db import transaction
from django.core.management.base import BaseCommand
from mixer.backend.django import mixer

from users.models import User
from ...factory import (
    UserFactory
)

NUM_USERS = 100
NUM_CLUBS = 10
NUM_THREADS = 12
COMMENTS_PER_THREAD = 25
USERS_PER_CLUB = 8

class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")

        self.stdout.write("Creating new data...")
        # Create all the users
        # for _ in range(NUM_USERS):
        #     person = UserFactory()
        #     print(_)
        user = mixer.cycle(5000).blend('users.User')
