from django.urls import path
from . import views


app_name = 'blog'


urlpatterns = [
    path('', views.ArticleListView.as_view(), name='root'),

    path('articles/', views.ArticleListView.as_view(), name='articles_list'),

    path('articles/<int:pk>/', views.article_detail, name='article_detail'),

    path('articles/create/', views.ArticleCreateView.as_view(), name='article_form_create'),

    path('articles/<int:pk>/update/', views.ArticleUpdateView.as_view(), name='article_form_edit'),

    path('articles/<int:pk>/delete/', views.ArticleDeleteView.as_view(), name='article_confirm_delete'),

    path('comments/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_confirm_delete'),
]

