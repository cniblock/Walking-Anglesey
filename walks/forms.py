from django import forms
from .models import Comment, NewsletterSubscriber, Post

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

class PostForm(forms.ModelForm):
    content_template = """
    <h1>Words & Photograph by </h1>
    <h2>Starting Point:</h2>
    <h2>Route Distance</h2>
    <h2>Detailed Walk Description</h2>
    <h2>Points of Interest</h2>
    <h2>Practical Information</h2>
    """

    class Meta:
        model = Post
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        if self.instance and not self.instance.pk:
            self.fields['content'].initial = self.content_template