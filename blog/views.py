from rest_framework import generics
from .models import BlogPost
from .serializers import BlogPostSerializer

# BlogPost GET API
class BlogPostListAPIView(generics.ListAPIView):
    queryset = BlogPost.objects.all().order_by('-created_at')
    serializer_class = BlogPostSerializer
