from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Article


class ArticleListView(ListView):
    model = Article
    context_object_name = 'articles'
    ordering = ['-created_at']


class ArticleDetailView(DetailView):
    model = Article
    context_object_name = 'article'


class ArticleCreateView(CreateView):
    model = Article
    fields = ['title', 'body']
    template_name = 'blog/article_form_create.html'

    def get_success_url(self) -> str:
        return reverse('blog:article_path', kwargs={'pk': self.object.pk})


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ['title', 'body']
    template_name = 'blog/article_form_edit.html'

    def get_success_url(self) -> str:
        return reverse('blog:article_path', kwargs={'pk': self.object.pk})


class ArticleDeleteView(DeleteView):
    model = Article
    context_object_name = 'article'
    success_url = '/'
