from django import forms

from .models import Post, Comment

# Create your tests here.

class PostForm(forms.ModelForm):

	class Meta:
		model = Post                #어떤모델쓸래
		fields = ('title', 'text',) #뭐 입력받을래

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ( 'author', 'text',)