from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
      """Serializer for my extremely wicked Post Model"""
      class Meta:
            model = Post
            fields = ['id', 'title', 'body']
            read_only_fields =['id']