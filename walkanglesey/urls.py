from django.contrib import admin
from django.urls import path, include
from walks import views as walks_views

urlpatterns = [
    path("about/", include("about.urls"), name="about-urls"),
    path("accounts/", include("allauth.urls")),
    path("admin/", admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path("", include("walks.urls"), name="walks-urls"),
]

handler403 = 'walks.views.custom_403_view'
handler404 = 'walks.views.custom_404_view'
handler500 = 'walks.views.custom_500_view'