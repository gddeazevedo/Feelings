from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Article, Comment
from .forms import CommentForm


def article_detail(request: HttpRequest, pk: int):
    article = Article.objects.get(pk=pk)

    if request.method == 'GET':
        form = CommentForm()
    elif request.method == 'POST':
        form = CommentForm(data=request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.commenter = request.user
            comment.save()
            return redirect(to='blog:article_detail', pk=pk)

    context = {'article': article, 'comment_form': form}
    return render(request, 'blog/article_detail.html', context)


class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    context_object_name = 'articles'
    ordering = ['-created_at']

    # def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
    #     return super().get(request, *args, **kwargs)


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    fields = ['title', 'body']
    template_name = 'blog/article_form_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self) -> str:
        return reverse('blog:article_detail', kwargs={'pk': self.object.pk})


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = ['title', 'body']
    template_name = 'blog/article_form_edit.html'

    def form_valid(self, form) -> HttpResponse:
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        article = self.get_object()
        return self.request.user == article.author

    def get_success_url(self) -> str:
        return reverse('blog:article_detail', kwargs={'pk': self.object.pk})


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    context_object_name = 'article'
    success_url = '/'

    def test_func(self):
        article = self.get_object()
        return self.request.user == article.author


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    context_object_name = 'comment'

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.commenter

    def get_success_url(self) -> str:
        return reverse('blog:article_detail', kwargs={'pk': self.object.article.pk})
