from django.urls import path
from .views import PortfolioItemListAPIView

urlpatterns = [
    path('get/', PortfolioItemListAPIView.as_view(), name='portfolioitem-list'),
]
