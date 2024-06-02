from . import views
from django.urls import path
from .views import subscribe_newsletter, like_post

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('subscribe/', subscribe_newsletter, name='subscribe_newsletter'),
    path('walkslist/', views.walkslist, name='walkslist'),
    path('<slug:slug>/', views.post_detail, name='post_detail'), 
    path('<slug:slug>/edit_comment/<int:comment_id>', views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>', views.comment_delete),
    path('like/<int:post_id>/', like_post, name='like_post'),
]