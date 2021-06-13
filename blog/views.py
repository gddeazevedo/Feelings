from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import HttpRequest
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Article, Comment
from .forms import CommentForm


class ArticleListView(ListView):
    model = Article
    context_object_name = 'articles'
    ordering = ['-created_at']


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
            return redirect(to='blog:article_path', pk=pk)

    context = {'article': article, 'comment_form': form}
    return render(request, 'blog/article_detail.html', context)


class ArticleCreateView(CreateView):
    model = Article
    fields = ['title', 'body']
    template_name = 'blog/article_form_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

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


class CommentDeleteView(DeleteView):
    model = Comment
    context_object_name = 'comment'

    def get_success_url(self) -> str:
        return reverse('blog:article_path', kwargs={'pk': self.object.article.pk})
