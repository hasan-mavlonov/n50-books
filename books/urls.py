from django.urls import path
from books.views import home_page

urlpatterns = [
    path('', home_page),
]
