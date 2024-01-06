from django.views.generic import ListView
from books.models import Book
from members.models import Member
from issues.models import Issue
from django.contrib.auth.mixins import LoginRequiredMixin


class HomePageView(LoginRequiredMixin, ListView):
    model = Book
    template_name = "books.html"


class MembersView(LoginRequiredMixin, ListView):
    model = Member
    template_name = "members.html"


class IssuesView(LoginRequiredMixin, ListView):
    model = Issue
    template_name = "issues.html"
