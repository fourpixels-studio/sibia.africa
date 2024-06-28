from django.shortcuts import get_object_or_404, redirect, render
from .models import Article, SDG
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm, SDGForm, EditSDGForm
from django.contrib import messages


@login_required(login_url='/account/signin/')
def edit_article(request, pk):
    # Initialize context as an empty dictionary
    context = {}

    try:
        # Try to get the article using its slug or set article to None if not found
        article = get_object_or_404(Article, pk=pk)
    except Article.DoesNotExist:
        article = None

    # Initialize the update article form with POST and FILES data if available, using the article instance
    edit_article_form = ArticleForm(
        request.POST or None, request.FILES or None, instance=article)

    # Handle form submission if the request method is POST
    if request.method == "POST":
        # Check if the update article form is valid
        if edit_article_form.is_valid():
            # Save the form but don't commit changes to the database yet
            edit_article = edit_article_form.save(commit=False)

            # Save the updated article to the database
            edit_article.save()

            # Display a success message and redirect to the article detail page
            messages.info(request, "This article has been updated!")
            return redirect("article_detail", article.slug)
        else:
            messages.info(request, "Failed to update")
    else:
        # If the request method is not POST, use the update article form with the article instance
        edit_article_form = ArticleForm(instance=article)

    context = {
        "title_tag": f"Editing {article.title}",
        "article": article,
        "edit_article_form": edit_article_form,
        "user": request.user,
    }
    return render(request, "crud_pages/edit_article.html", context)


@login_required(login_url='/account/signin/')
def new_article(request):
    author = request.user
    if request.method == "POST":
        new_article_form = ArticleForm(
            request.POST or None, request.FILES or None)
        if new_article_form.is_valid():
            if author:
                article = new_article_form.save(commit=False)
                article.author = author
                article.save()
                messages.info(request, "Succesfully added article")
                return redirect("article_list")
    else:
        new_article_form = ArticleForm()

    context = {
        "title_tag": "Create New Article",
        "new_article_form": new_article_form,
    }
    return render(request, "crud_pages/new_article.html", context)


@login_required(login_url='/account/signin/')
def new_sdg(request):
    if request.method == "POST":
        new_sdg_form = SDGForm(request.POST or None)
        if new_sdg_form.is_valid():
            sdg = new_sdg_form.save(commit=False)
            name = sdg.name
            sdg.save()
            messages.info(request, f"Succesfully added  '{name}'")
            return redirect("new_sdg")
    else:
        new_sdg_form = SDGForm()

    context = {
        "title_tag": "Create New SDG",
        "new_sdg_form": new_sdg_form,
        "sdgs": SDG.objects.order_by("-pk"),
    }
    return render(request, "crud_pages/new_sdg.html", context)


@login_required(login_url='/account/signin/')
def edit_sdg(request, pk):
    sdg = get_object_or_404(SDG, pk=pk)
    if request.method == "POST":
        edit_sdg_form = EditSDGForm(request.POST or None)
        if edit_sdg_form.is_valid():
            sdg = edit_sdg_form.save(commit=False)
            name = sdg.name
            sdg.save()
            messages.info(request, f"'{name}' was succesfully updated!")
            return redirect("edit_sdg", sdg.pk)
    else:
        edit_sdg_form = EditSDGForm()

    context = {
        "sdg": sdg,
        "edit_sdg_form": edit_sdg_form,
        "title_tag": f"Editing: {sdg.name}",
        "sdgs": SDG.objects.all(),
    }
    return render(request, "crud_pages/edit_sdg.html", context)


@login_required(login_url='/account/signin/')
def edit_sdg(request, pk):
    # Initialize context as an empty dictionary
    context = {}

    try:
        # Try to get the sdg using its slug or set sdg to None if not found
        sdg = get_object_or_404(SDG, pk=pk)
    except SDG.DoesNotExist:
        sdg = None

    # Initialize the update sdg form with POST and FILES data if available, using the sdg instance
    edit_sdg_form = EditSDGForm(request.POST or None, instance=sdg)

    # Handle form submission if the request method is POST
    if request.method == "POST":
        # Check if the update sdg form is valid
        if edit_sdg_form.is_valid():
            # Save the form but don't commit changes to the database yet
            edit_sdg = edit_sdg_form.save(commit=False)

            # Save the updated sdg to the database
            edit_sdg.save()

            # Display a success message and redirect to the sdg detail page
            messages.info(request, f"'{sdg.name}' has been updated!")
            return redirect("edit_sdg", sdg.pk)
        else:
            messages.info(request, "Failed to update")
    else:
        # If the request method is not POST, use the update sdg form with the sdg instance
        edit_sdg_form = EditSDGForm(instance=sdg)

    context = {
        "sdg": sdg,
        "edit_sdg_form": edit_sdg_form,
        "title_tag": f"Editing: {sdg.name}",
        "sdgs": SDG.objects.all(),
    }
    return render(request, "crud_pages/edit_sdg.html", context)
