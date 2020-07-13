from django.urls import path
from main.views import TagsListView, TagView, FullPageView, TelegramView
urlpatterns = [
    path('form/', TelegramView),
    path('FullPage/', FullPageView.as_view()),
    path('tag/', TagsListView.as_view()),
    path('tag/<int:pk>', TagView.as_view())
]