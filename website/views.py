from django.shortcuts import render, redirect
from .forms import NewsletterSubscriptionForm
from django.contrib import messages


def index(request):
    context = {
        "title_tag": "Home",
    }
    return render(request, "index.html", context)


def about(request):
    context = {
        "title_tag": "About Us",
    }
    return render(request, "about.html", context)


def contact(request):
    context = {
        "title_tag": "Contact Us",
    }
    return render(request, "contact.html", context)


def newsletter_subscription(request):
    if request.method == 'POST':
        form = NewsletterSubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you for subscribing")
            return redirect('index')
    else:
        form = NewsletterSubscriptionForm()
    return render(request, 'index.html', {'form': form})
