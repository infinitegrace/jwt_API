from django.urls import path
from .views import Registerview, LoginView, UserView 


urlpatterns = [
    path('register/', Registerview.as_view()),
    path('login/', LoginView.as_view()),
    path('user/', UserView.as_view()),
    path('logout/', LogoutView.as_view())


] 
