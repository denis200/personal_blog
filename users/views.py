from django.shortcuts import render
from rest_framework import views,permissions,response

from .models import User,UserFollowing

class FollowerView(views.APIView):
    """ Добавление в подписчики
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        try:
            user = User.objects.get(id=pk)
        except User.DoesNotExist:
            return response.Response({'Bad Request': "User not found"},status=404)
        obj, created = UserFollowing.objects.get_or_create(following_user_id=request.user, user_id=user)
        if not created:
            return response.Response({'Warning':'You are already following this user'},status=403)
        return response.Response({'Success':'You subscribed to this user '},status=201)

    def delete(self, request, pk):
        try:
            sub = UserFollowing.objects.get(following_user_id=request.user, user_id=pk)
        except UserFollowing.DoesNotExist:
            return response.Response({"Bad Request":"You are not following this user"},status=404)
        sub.delete()
        return response.Response({"Success":"You unfollowed this user"},status=204)
