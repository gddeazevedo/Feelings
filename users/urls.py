from django.urls import path
from django.contrib.auth.views import LoginView
from . import views


app_name = 'users'

urlpatterns = [
    # /users/signup
    path('signup/', views.sign_up, name='user_signup_path'),
    
    # /users/signin
    path('signin/', LoginView.as_view(template_name='users/sign-in.html'), name='user_login_path'),

    # /users/logout
    path('logout/', views.logout, name='user_logout_path')
]
