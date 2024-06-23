from django.shortcuts import render


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
