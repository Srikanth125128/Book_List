from django.urls import path
from .api import BookListAPIView

urlpatterns = [
    path('books/', BookListAPIView.as_view()),
]
