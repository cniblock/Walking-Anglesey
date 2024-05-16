from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post

# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "walks/index.html"
    paginate_by = 6


def post_detail(request, slug):
    """
    Display an individual :model:`walks.Post`.

    **Context**

    ``post``
        An instance of :model:`walks.Post`.

    **Template:**

    :template:`walks/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "walks/post_detail.html",
        {"post": post},
    )