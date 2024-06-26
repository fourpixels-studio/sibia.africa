from django.shortcuts import get_object_or_404, redirect, render
from .models import Homepage
from django.contrib.auth.decorators import login_required
from .forms import HomepageForm
from django.contrib import messages


@login_required(login_url='/account/signin/')
def edit_homepage(request, pk):
    context = {}

    try:
        homepage = get_object_or_404(Homepage, pk=pk)
    except Homepage.DoesNotExist:
        homepage = None

    edit_homepage_form = HomepageForm(
        request.POST or None, request.FILES or None, instance=homepage)

    if request.method == "POST":

        if edit_homepage_form.is_valid():
            edit_homepage = edit_homepage_form.save(commit=False)
            edit_homepage.save()
            messages.info(request, "Homepage has been updated!")
            return redirect("index")
        else:
            messages.info(request, "Failed to update")
    else:
        edit_homepage_form = HomepageForm(instance=homepage)

    context = {
        "title_tag": "Editing Homepage",
        "homepage": homepage,
        "edit_homepage_form": edit_homepage_form,
    }
    return render(request, "crud_pages/edit_homepage.html", context)
