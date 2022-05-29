from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer
from .models import Post

class PostViewSet(ModelViewSet):
      """Handles all functions for the Post API"""
      queryset = Post.objects.all()
      serializer_class = PostSerializer

      