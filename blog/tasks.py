from config.celery import app
from .services import feed_service


@app.task
def get_last_posts_task(user_id,number_of_posts):
    """ Задача рассылки последних постов """
    for post in feed_service.get_post_list(user_id,number_of_posts):
        print(f"Заголовок: {post.title}")
        print(f"Текст: {post.text}")