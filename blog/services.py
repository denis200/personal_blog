from django.conf import settings
from .models import Blog, Post


class Feed:
    """ Service feeds
    """
    def get_post_list(self, user, limit = 500):
        # return Post.objects.filter(blog__following__following_user_id = user)
        return Post.objects.filter(blog__following__following_user_id = user.id).order_by('-created').exclude(views__user = user)[:limit]

    def get_single_post(self, pk: int):
        return Post.objects.select_related('user').get(id=pk)


feed_service = Feed()