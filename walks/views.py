import requests 
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment, NewsletterSubscriber
from .forms import CommentForm, NewsletterSubscriptionForm
from django.contrib.auth.decorators import login_required
from django.conf import settings
import random

def custom_403_view(request, exception):
    return render(request, "403.html", {}, status=403)

def custom_404_view(request, exception):
    return render(request, "404.html", {}, status=404)

def custom_500_view(request):
    return render(request, "500.html", status=500)

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('?')
    template_name = "walks/index.html"
    paginate_by = 6

def get_weather(location):
    api_key = settings.OPENWEATHERMAP_API_KEY
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "q=" + location + "&appid=" + api_key + "&units=metric"
    response = requests.get(complete_url)
    return response.json()

def post_detail(request, slug):
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )
    comment_form = CommentForm()  

    # Fetch weather data for the location
    weather_data = get_weather("Anglesey")

    return render(
        request,
        "walks/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
            "weather_data": weather_data,
        },
    )

@login_required
def comment_edit(request, slug, comment_id):
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author != request.user:
        messages.add_message(request, messages.ERROR, 'You cannot edit comments that are not yours!')
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST, instance=comment)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment updated successfully!')
            return HttpResponseRedirect(reverse('post_detail', args=[slug]))
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')
    else:
        comment_form = CommentForm(instance=comment)

    return render(request, 'walks/comment_edit.html', {'comment_form': comment_form, 'post': post, 'comment': comment})

@login_required
def comment_delete(request, slug, comment_id):
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author != request.user:
        messages.add_message(request, messages.ERROR, 'You cannot delete comments that are not yours!')
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))

    comment.delete()
    messages.add_message(request, messages.SUCCESS, 'Comment deleted successfully!')
    
    return HttpResponseRedirect(reverse('post_detail', args=[slug]))

def walkslist(request):
    posts = Post.objects.all()
    hero_image = None
    if posts:
        random_post = random.choice(posts)
        hero_image = random_post.featured_image.url

    context = {
        'posts': posts,
        'hero_image': hero_image,
    }
    return render(request, 'walks/walkslist.html', context)

def subscribe_newsletter(request):
    posts = Post.objects.all()
    hero_image = None
    if posts.exists():
        random_post = random.choice(posts)
        hero_image = random_post.featured_image.url

    if request.method == "POST":
        form = NewsletterSubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have successfully subscribed to the newsletter.")
            return redirect('home')
    else:
        form = NewsletterSubscriptionForm()

    context = {
        'form': form,
        'hero_image': hero_image,
    }
    
    return render(request, 'walks/subscribe_newsletter.html', context)
