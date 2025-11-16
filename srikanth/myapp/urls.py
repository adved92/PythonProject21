from django.urls import path
from .views import register_user, user_login, user_logout, create_user

urlpatterns = [
    path('register/', register_user, name='register'),  # Ensure this is defined
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('create-user/', create_user, name='create-user'),
]
