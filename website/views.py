from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from .forms import NewsletterSubscriptionForm, AppointmentForm
from .models import Homepage, PrivacyPolicy, TermsOfService, FrequentlyAskedQuestion, Help


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


def help(request):
    try:
        faq_data = get_object_or_404(Help, pk=1)
    except:
        faq_data = None

    try:
        privacy_policy_data = get_object_or_404(Help, pk=2)
    except:
        privacy_policy_data = None

    try:
        terms_of_service_data = get_object_or_404(Help, pk=3)
    except:
        terms_of_service_data = None

    if privacy_policy_data:
        privacy_policy_title = privacy_policy_data.title
        privacy_policy_paragraph = privacy_policy_data.paragraph
    else:
        privacy_policy_title = "Privacy Policy for Sibia"
        privacy_policy_paragraph = 'Thank you for choosing to be part of our community at Sibia ("Company, " "we, " "us, " "our"). We are committed to protecting your personal information and your right to privacy.'

    if faq_data:
        faq_title = faq_data.title
        faq_paragraph = faq_data.paragraph
    else:
        faq_title = "Frequently Asked Questions"
        faq_paragraph = "These are general questions we get time to time. Contact us if you cant find the answers you're looking for"

    if terms_of_service_data:
        terms_of_service_title = terms_of_service_data.title
        terms_of_service_paragraph = terms_of_service_data.paragraph
    else:
        terms_of_service_title = "Terms of Service"
        terms_of_service_paragraph = "These Terms of Service govern your use of Sibia. By accessing or using our website, you agree to be bound by these Terms of Service. If you do not agree to these terms, you may not use our website."

    context = {
        "title_tag": "Help Centre",
        "policies": PrivacyPolicy.objects.all(),
        "terms_of_services": TermsOfService.objects.all(),
        "frequently_asked_questions": FrequentlyAskedQuestion.objects.all(),
        "faq_title": faq_title,
        "faq_paragraph": faq_paragraph,
        "privacy_policy_title": privacy_policy_title,
        "privacy_policy_paragraph": privacy_policy_paragraph,
        "terms_of_service_title": terms_of_service_title,
        "terms_of_service_paragraph": terms_of_service_paragraph,
    }
    return render(request, "help.html", context)


def request_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Appointment confirmed! We have received your request and will contact you shortly with the details. Thank you for your trust.")
            return redirect('index')
    else:
        form = AppointmentForm()

    return render(request, 'contact.html', {'form': form})
