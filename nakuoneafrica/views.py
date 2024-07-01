from django.shortcuts import render, get_object_or_404
from .models import SDG, Article


def nakuoneafrica(request):

    context = {
        "title_tag": "Naku-One Africa",
        "sdgs": SDG.objects.all(),
        "articles": Article.objects.order_by('-pk'),
        "meta_description": "Find out how Naku One Africa is advancing the awareness, knowledge and  implementation of the sustainable development goals",
        "meta_keywords": "Sustainable Development, Community Hospital, Informal Settlements, Vulnerable Communities, Global South, SDGs, Research and Development, AI Studio, Data Analytics Lab, Community Health, Social Impact, Environmental Sustainability, Education and Innovation, Healthcare Access, Poverty Alleviation",
    }

    return render(request, "nakuoneafrica.html", context)


def article_list(request):

    context = {
        "title_tag": "Articles | Naku-One Africa",
        "articles": Article.objects.order_by('-pk'),
        "meta_description": "Read our latest articles. Find out how Naku One Africa is advancing the awareness, knowledge and  implementation of the sustainable development goals",
        "meta_keywords": "Sustainable Development, Community Hospital, Informal Settlements, Vulnerable Communities, Global South, SDGs, Research and Development, AI Studio, Data Analytics Lab, Community Health, Social Impact, Environmental Sustainability, Education and Innovation, Healthcare Access, Poverty Alleviation",
    }

    return render(request, "article_list.html", context)


def articles_listed_by_sdg(request, slug):
    sdg = get_object_or_404(SDG, slug=slug)
    articles = Article.objects.filter(sdg=sdg, is_published=True)
    context = {
        "title_tag": f"Goal {sdg.pk}: {sdg} Articles | Naku-One Africa",
        "articles": articles,
        "sdg": sdg,
        "active_sdg": sdg,
        "sdgs": SDG.objects.all(),
        "meta_description": f"Read our latest articles in {sdg}. Find out how Naku One Africa is advancing the awareness, knowledge and  implementation of the sustainable development goals",
        "meta_keywords": f"{sdg}, Sustainable Development, Community Hospital, Informal Settlements, Vulnerable Communities, Global South, SDGs, Research and Development, AI Studio, Data Analytics Lab, Community Health, Social Impact, Environmental Sustainability, Education and Innovation, Healthcare Access, Poverty Alleviation",
    }

    return render(request, "article_list.html", context)


def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    if article.meta_thumbnail:
        meta_thumbnail = article.meta_thumbnail.url
    else:
        meta_thumbnail = None
    author = article.author.first_name
    context = {
        "articles": Article.objects.order_by('-pk'),
        "sdgs": SDG.objects.all(),
        "article": article,
        "author": author,
        "title_tag": f"Goal {article.sdg.pk}: {article.title}",
        "meta_description": article.summary,
        "meta_thumbnail": meta_thumbnail,
        "meta_keywords": f"{article.sdg.name}, Sustainable Development, Community Hospital, Informal Settlements, Vulnerable Communities, Global South, SDGs, Research and Development, AI Studio, Data Analytics Lab, Community Health, Social Impact, Environmental Sustainability, Education and Innovation, Healthcare Access, Poverty Alleviation",
    }

    return render(request, "article_detail.html", context)

