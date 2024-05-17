from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import About
from django_summernote.admin import SummernoteModelAdmin


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)