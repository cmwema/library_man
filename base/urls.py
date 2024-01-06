from django.urls import path
from .views import HomePageView, MembersView, IssuesView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("members/", MembersView.as_view(), name="members"),
    path("issues/", IssuesView.as_view(), name="issues"),
]
