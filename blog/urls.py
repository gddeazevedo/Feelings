from django.urls import path
from .views import (
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView
)


app_name = 'blog'

urlpatterns = [
    # /
    path('', ArticleListView.as_view(), name='root_path'),

    # /articles
    path('articles/', ArticleListView.as_view(), name='articles_path'),

    # /articles/:id
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='article_path'),

    # /articles/new
    path('articles/new/', ArticleCreateView.as_view(), name='new_article_path'),

    # /articles/:id/edit
    path('articles/<int:pk>/edit/', ArticleUpdateView.as_view(), name='edit_article_path'),

    # /articles/:id/delete
    path('articles/<int:pk>/delete/', ArticleDeleteView.as_view(), name='delete_article_path'),
]
