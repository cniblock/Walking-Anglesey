from django import forms
from .models import Comment, NewsletterSubscriber

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class NewsletterSubscriptionForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscriber
        fields = ['email']

class NewsletterForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)