from django.urls import path
from .views import news_portal_view

urlpatterns = [
    path('news/', news_portal_view, name='news_portal'),
]
