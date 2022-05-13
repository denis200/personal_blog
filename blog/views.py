from rest_framework import viewsets,permissions,response,status
from . import serializers,models

class PostView(viewsets.ModelViewSet):
    
    """ CRUD карточек товара"""
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return models.Post.objects.all()
    