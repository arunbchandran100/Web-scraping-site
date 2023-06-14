from django.db import models

class real_estate(models.Model):
    title=models.Charfield(max_length=150)
    price=models.Charfield(max_length=30)
    location=models.Charfield(max_length=150)
    square_foot=models.Charfield(max_length=20)
    def __str__(self):
        return self.user