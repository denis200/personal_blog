from rest_framework import serializers
from . import models

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = ('__all__')


class ListPostSerializer(serializers.ModelSerializer):
    """ Список постов
    """

    class Meta:
        model = models.Post
        fields = ("id", "created", "blog", "title", "text")