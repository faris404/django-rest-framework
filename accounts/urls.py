from . import views
from django.urls import path

urlpatterns = [
   path('', views.Profile.as_view()),
   path('login', views.Login.as_view()),
   path('signup', views.Signup.as_view()),
]
