from django.shortcuts import render, redirect
from .forms import NewsletterSubscriptionForm
from django.contrib import messages
from .models import Homepage
from django.http import HttpResponse


def index(request):

    try:
        homepage_data = Homepage.objects.first()

        if not homepage_data:
            raise ValueError("No Homeage object found.")

        context = {
            "homepage_data": homepage_data,
            "title_tag": "Revolutionizing Community Healthcare with AI",
            "meta_description": "Sibia integrates a community health hospital, SDG research center, and advanced medical AI to serve informal communities with personalized therapies, illness control, and predictive analytics.",
            "meta_keywords": "Sibia, community healthcare, medical AI, SDG research, personalized therapies, illness control, predictive analytics, healthcare solutions, sustainable development goals",
        }

        return render(request, "index.html", context)

    except Homepage.DoesNotExist:
        return HttpResponse("Homeage not found.", status=404)

    except Exception as e:
        return HttpResponse("An error occurred while processing the request.", status=500)


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
