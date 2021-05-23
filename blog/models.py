from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    '''Represents the articles table in the database'''
    title = models.CharField(max_length=200)
    body = models.TextField(max_length=1000)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    '''Represents the comments table in the database'''
    commenter = models.ForeignKey(to=User, on_delete=models.CASCADE)
    article = models.ForeignKey(to=Article, on_delete=models.CASCADE)
    body = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if len(self.body) >= 10:
            body = self.body + '...'
        else:
            body = self.body
        return f'{self.commenter.username}: {body}'
