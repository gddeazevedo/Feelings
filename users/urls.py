from django.urls import path
from django.contrib.auth.views import LoginView
from . import views


app_name = 'users'

urlpatterns = [
    path('signup/', views.sign_up, name='user_signup_path'),
    path('signin/', LoginView.as_view(template_name='users/sign-in.html'), name='user_login_path'),
]
