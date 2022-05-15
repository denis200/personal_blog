from .models import Post


class Feed:
    """ Сервис формирования ленты постов людей, 
        на которых подписан пользователь
    """
    def get_post_list(self, user_id, limit = 500):
        return Post.objects.filter(blog__following__following_user_id = user_id).order_by('-created')\
            .exclude(views__user = user_id)[:limit]

    def get_single_post(self, pk: int):
        return Post.objects.select_related('user').get(id=pk)


feed_service = Feed()