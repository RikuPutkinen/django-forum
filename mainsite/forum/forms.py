from django import forms

class PostForm(forms.Form):
    nickname = forms.CharField(label="Nickname", max_length=20)
    post_title = forms.CharField(label="Title", max_length=50)
    post_text = forms.CharField(label="Text", widget=forms.Textarea())

class CommentForm(forms.Form):
    nickname = forms.CharField(label="Nickname", max_length=20)
    comment_text = forms.CharField(label="Text", widget=forms.Textarea())