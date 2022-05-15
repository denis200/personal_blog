import json
from django_celery_beat.models import PeriodicTask,IntervalSchedule


def create_task(user_id):
    """ Создание задачи celery
    """
    number_of_posts = 5
    schedule,_ = IntervalSchedule.objects.get_or_create(every=1, period=IntervalSchedule.DAYS)
    PeriodicTask.objects.create(
          name=f'{user_id} | EveryDay Posts Mail',
          task='blog.tasks.get_last_posts_task',
          interval = schedule,
          args = json.dumps([user_id,number_of_posts]),
        )