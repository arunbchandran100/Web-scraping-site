from django.contrib.auth.models import User
from django.db import models

class Listing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    price = models.CharField(max_length=50)
    location = models.CharField(max_length=255)
    more_details_link = models.URLField()
    square_footage = models.CharField(max_length=50)
    image_urls = models.TextField()

    # Add any other fields or methods as needed

    def __str__(self):
        return self.title
