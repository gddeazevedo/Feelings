from django.urls import path
from django.contrib.auth.views import LoginView
from . import views


app_name = 'users'

urlpatterns = [
    path('signup/', views.sign_up, name='sign_up'),
    
    path('signin/', LoginView.as_view(template_name='users/sign_in.html'), name='sign_in'),

    path('signout/', views.sign_out, name='sign_out')
]
