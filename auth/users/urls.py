from django.urls import path
from .views import Registerview, LoginView 


urlpatterns = [
    path('register/', Registerview.as_view()),
    path('login/', LoginView.as_view())

] 
