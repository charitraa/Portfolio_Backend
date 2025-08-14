from uuid import uuid4
from django.db import models

# Create your models here.
class PortfolioItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio_images/', blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title