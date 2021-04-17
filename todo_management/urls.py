from . import views
from django.urls import path

urlpatterns = [
   path('', views.TodoList.as_view()),
]
