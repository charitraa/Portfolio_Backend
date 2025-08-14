from django.urls import path
from .views import BlogPostListAPIView

urlpatterns = [
    path('get/', BlogPostListAPIView.as_view(), name='blogpost-list'),
]
