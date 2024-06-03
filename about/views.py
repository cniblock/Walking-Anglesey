from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import CollaborateForm

def about_me(request):
    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(request, 
            messages.SUCCESS, "Collaboration request received! We will endeavour to respond within 2 working days.")
        else:
            messages.add_message(request, 
            messages.ERROR, "There was an error with your submission. Please check the form and try again.")
    else:
        collaborate_form = CollaborateForm()

    about = About.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "about/about.html",
        {"about": about,
        "collaborate_form": collaborate_form
        },
    )