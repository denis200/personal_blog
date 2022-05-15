from rest_framework import views,permissions,response

from blog.models import Blog
from .models import UserFollowing

class FollowerView(views.APIView):
    """ Подписка на блог пользователя
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        """ Создание подписки"""
        try:
            blog = Blog.objects.get(id=pk)
        except Blog.DoesNotExist:
            return response.Response({'Bad Request': "Blog not found"},status=404)
        obj, created = UserFollowing.objects.get_or_create(following_user_id=request.user, blog_id=pk)
        if not created:
            return response.Response({'Warning':'You are already following this blog'},status=403)
        return response.Response({'Success':'You subscribed to this blog '},status=201)

    def delete(self, request, pk):
        """ Удаление подписки"""
        try:
            sub = UserFollowing.objects.get(following_user_id=request.user, blog_id=pk)
        except UserFollowing.DoesNotExist:
            return response.Response({"Bad Request":"You are not following this blog"},status=404)
        sub.delete()
        return response.Response({"Success":"You unfollowed this blog"},status=204)
