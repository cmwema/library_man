from django.db import models


class Member(models.Model):
    name = models.CharField(max_length=255)
    debt = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
