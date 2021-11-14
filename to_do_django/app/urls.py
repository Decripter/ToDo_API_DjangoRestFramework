from django.urls import path
from django.urls.resolvers import URLPattern
from app.views import TodoListAndCreate, TodoDetailChangeAndDelete
urlpatterns = [
    path('', TodoListAndCreate.as_view()),
    path('<int:pk>/', TodoDetailChangeAndDelete.as_view()),
]
