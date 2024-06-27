from django.shortcuts import render, get_object_or_404
from .models import SDG, Article


def nakuoneafrica(request):

    context = {
        "title_tag": "Naku-One Africa",
        "sdgs": SDG.objects.all(),
        "articles": Article.objects.order_by('-pk'),
        "meta_description": "Find out how Naku One Africa is advancing the awareness, knowledge and implementation of the sustainable development goals.",
        "meta_keywords": "Sustainable Development, Community Hospital, Informal Settlements, Vulnerable Communities, Global South, SDGs, Research and Development, AI Studio, Data Analytics Lab, Community Health, Social Impact, Environmental Sustainability, Education and Innovation, Healthcare Access, Poverty Alleviation",
    }

    return render(request, "nakuoneafrica.html", context)


def article_list(request):

    context = {
        "title_tag": "Articles | Naku-One Africa",
        "articles": Article.objects.order_by('-pk'),
        "meta_description": "",
        "meta_keywords": "",
    }

    return render(request, "article_list.html", context)


def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    context = {
        "title_tag": article.title,
        "articles": Article.objects.order_by('-pk'),
        "article": article,
        "meta_description": "",
        "meta_keywords": "", }

    return render(request, "article_detail.html", context)
