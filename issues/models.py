from django.db import models
from books.models import Book
from members.models import Member


class Issue(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    returned = models.DateTimeField(auto_now=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.date}"
