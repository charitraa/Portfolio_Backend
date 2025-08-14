# Create your views here.
from rest_framework import generics
from .models import PortfolioItem
from .serializers import  PortfolioItemSerializer

# PortfolioItem GET API
class PortfolioItemListAPIView(generics.ListAPIView):
    queryset = PortfolioItem.objects.all().order_by('-created_at')
    serializer_class = PortfolioItemSerializer
