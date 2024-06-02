from django.contrib import admin
from django.core.mail import send_mail
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import path
from django.shortcuts import render
from .models import Post, Comment, NewsletterSubscriber
from django_summernote.admin import SummernoteModelAdmin
from .forms import NewsletterForm

BATCH_SIZE = 10

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on', 'difficulty')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on', 'difficulty')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'author', 'featured_image', 'route_image', 'content', 'excerpt', 'status', 'difficulty')
        }),
    )

admin.site.register(Comment)

@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_subscribed')
    search_fields = ['email']
    list_filter = ('date_subscribed',)
    actions = ['send_newsletter']

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('send_newsletter/', self.admin_site.admin_view(self.send_newsletter_view), name='send_newsletter'),
        ]
        return custom_urls + urls

    def send_newsletter_view(self, request):
        if request.method == 'POST':
            form = NewsletterForm(request.POST)
            if form.is_valid():
                subject = form.cleaned_data['subject']
                message = form.cleaned_data['message']
                recipients = list(NewsletterSubscriber.objects.values_list('email', flat=True))
                
                # Send emails in batches
                for i in range(0, len(recipients), BATCH_SIZE):
                    batch = recipients[i:i + BATCH_SIZE]
                    send_mail(subject, message, 'your_email@example.com', batch)
                
                self.message_user(request, "Newsletter is being sent successfully. Emails will be sent in batches.")
                return HttpResponseRedirect("../")
        else:
            form = NewsletterForm()

        context = {
            'form': form,
            'title': 'Send Newsletter'
        }
        return render(request, 'admin/send_newsletter.html', context)

    def send_newsletter(self, request, queryset):
        return HttpResponseRedirect('send_newsletter/')

    send_newsletter.short_description = 'Send Newsletter to Subscribers'

