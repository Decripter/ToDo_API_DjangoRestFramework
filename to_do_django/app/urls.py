from django.urls import path
from django.urls.resolvers import URLPattern
from app.views import todo_list
urlpatterns = [
    path('', todo_list)
]
