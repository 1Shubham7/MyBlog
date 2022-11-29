from django import forms
from blog_app.models import Post, Comment

class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('author','title','text')
        widgets = {
            'title':forms.TextInput(attrs={'class':'classno1'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }

class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('author','text')
        widgets = {
            'author':forms.TextInput(attrs={'class':'classno1'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'}),
        }
