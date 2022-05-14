from rest_framework import viewsets,permissions,response,status,views
from . import serializers,models
from .services import feed_service


class PostView(viewsets.ModelViewSet):
    
    """ CRUD карточек товара"""
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return models.Post.objects.all()


class FeedView(viewsets.GenericViewSet):
    """ View follower`s feed
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.ListPostSerializer

    def list(self, request, *args, **kwargs):
        queryset = feed_service.get_post_list(request.user.id)
        serializer = self.get_serializer(queryset, many=True)
        return response.Response(serializer.data)


class ReadPostView(views.APIView):
    """ Пометить пост прочитанным
    """
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, pk):
        try:
            post = models.Post.objects.get(id=pk)
        except models.Post.DoesNotExist:
            return response.Response({'Bad Request': "Post not found"},status=404)
        obj, created = models.ViewPost.objects.get_or_create(post=post, user=request.user)
        if not created:
            return response.Response({'Warning':'You have already seen this post'},status=403)
        return response.Response({'Success':'This post is viewed'},status=201)
    
    def delete(self, request, pk):
        try:
            post = models.ViewPost.objects.get(post=pk, user=request.user)
        except models.ViewPost.DoesNotExist:
            return response.Response({"Bad Request":"You have not viewed this post"},status=404)
        post.delete()
        return response.Response({"Success":"You have removed this post from your watch list"},status=204)
