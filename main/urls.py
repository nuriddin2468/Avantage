from django.urls import path
from main.views import TagsListView, TagView
urlpatterns = [
    path('tags/', TagsListView.as_view()),
    path('tag/<int:pk>', TagView.as_view())
]