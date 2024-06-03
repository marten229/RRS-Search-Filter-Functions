# restaurant_management/models.py
from django.db import models
from django.contrib.auth.models import User

class Restaurant(models.Model):
    CUISINE_CHOICES = [
        ('Italian', 'Italian'),
        ('Chinese', 'Chinese'),
        ('Mexican', 'Mexican'),
        ('Indian', 'Indian'),
        ('French', 'French'),
        ('Japanese', 'Japanese'),
        ('Thai', 'Thai'),
        ('Other', 'Other'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    address = models.TextField()
    city = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to='restaurant_photos/', blank=True, null=True)
    cuisine = models.CharField(max_length=50, choices=CUISINE_CHOICES)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
