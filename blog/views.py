from rest_framework import viewsets,permissions,response,status
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
        print(request.user.id)
        queryset = feed_service.get_post_list(request.user.id)
        serializer = self.get_serializer(queryset, many=True)
        return response.Response(serializer.data)
    