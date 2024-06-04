from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post, Comment, NewsletterSubscriber
from .forms import CommentForm, NewsletterSubscriptionForm

class TestPostViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        self.post = Post.objects.create(
            title="Post title",
            author=self.user,
            slug="post-title",
            excerpt="Post excerpt",
            content="Post content",
            status=1,
            featured_image="placeholder"
        )

    def test_render_post_detail_page_with_comment_form(self):
        response = self.client.get(reverse('post_detail', args=['post-title']))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Post title", response.content)
        self.assertIn(b"Post content", response.content)
        self.assertIsInstance(response.context['comment_form'], CommentForm)

    def test_render_post_list_page(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Post title", response.content)
        self.assertIn(b"Post excerpt", response.content)

    def test_render_post_list_page_with_placeholder_image(self):
        self.post.featured_image = "placeholder"
        self.post.save()
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertRegex(response.content.decode('utf-8'), r'src="/static/images/default\.\w+\.jpg"')

    def test_successful_comment_submission(self):
        """Test for a successful comment submission"""
        self.client.login(username="myUsername", password="myPassword")
        comment_data = {
            'name': 'test name',
            'email': 'test@email.com',
            'body': 'test comment'
        }
        response = self.client.post(reverse('post_detail', args=['post-title']), data=comment_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Comment submitted and awaiting approval', response.content)
        
    def test_successful_newsletter_subscription(self):
        post_data = {
            'email': 'test_subscriber@example.com',
        }
        response = self.client.post(reverse('subscribe_newsletter'), data=post_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
        self.assertTrue(NewsletterSubscriber.objects.filter(email='test_subscriber@example.com').exists())
