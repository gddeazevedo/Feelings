from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    '''A form for the Comment model'''

    class Meta:
        '''Nested class that specifies the form fields'''
        model  = Comment
        fields = ['body']
        labels = {'body': ''}
        widgets = {
            'body': forms.Textarea(attrs={'cols': 50, 'rows': 10})
        }
