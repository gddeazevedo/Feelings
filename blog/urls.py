from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [
    # /
    path('', views.ArticleListView.as_view(), name='root_path'),

    # /articles
    path('articles/', views.ArticleListView.as_view(), name='articles_path'),

    # /articles/:id
    path('articles/<int:pk>/', views.article_detail, name='article_path'),

    # /articles/new
    path('articles/new/', views.ArticleCreateView.as_view(), name='new_article_path'),

    # /articles/:id/edit
    path('articles/<int:pk>/edit/', views.ArticleUpdateView.as_view(), name='edit_article_path'),

    # /articles/:id/delete
    path('articles/<int:pk>/delete/', views.ArticleDeleteView.as_view(), name='delete_article_path'),
]
