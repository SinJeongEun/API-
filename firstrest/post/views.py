from rest_framework import viewsets
from .models import Post
from .serializer import PostSeriallizer

# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSeriallizer