from rest_framework import viewsets,permissions,response,status,views
from blog.models import Post, ViewPost
from . import serializers
from .services import feed_service


class PostView(viewsets.ModelViewSet):
    
    """ CRUD карточек товара"""
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Post.objects.all()


class FeedView(viewsets.GenericViewSet):
    """ View follower`s feed
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.ListPostSerializer

    def list(self, request, *args, **kwargs):
        queryset = feed_service.get_post_list(request.user.id)
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)


class ReadPostView(views.APIView):
    """ Пометить пост прочитанным
    """
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, pk):
        try:
            post = Post.objects.get(id=pk)
        except Post.DoesNotExist:
            return response.Response({'Bad Request': "Post not found"},status=404)
        obj, created = ViewPost.objects.get_or_create(post=post, user=request.user)
        if not created:
            return response.Response({'Warning':'You have already seen this post'},status=403)
        return response.Response({'Success':'This post is viewed'},status=201)
    
    def delete(self, request, pk):
        try:
            post = ViewPost.objects.get(post=pk, user=request.user)
        except ViewPost.DoesNotExist:
            return response.Response({"Bad Request":"You have not viewed this post"},status=404)
        post.delete()
        return response.Response({"Success":"You have removed this post from your watch list"},status=204)
