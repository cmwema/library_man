from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
