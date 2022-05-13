from django.conf import settings
from .models import Blog, Post


class Feed:
    """ Service feeds
    """
    def get_post_list(self, user):
        return Post.objects.filter(blog__user__following__following_user_id = user).order_by('-created').exclude(views__user = user)

    def get_single_post(self, pk: int):
        return Post.objects.select_related('user').get(id=pk)


feed_service = Feed()