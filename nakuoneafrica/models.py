from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django_resized import ResizedImageField
from django.urls import reverse


class SDG(models.Model):
    name = models.CharField(max_length=80)
    icon = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Category(models.Model):
    title = models.CharField(max_length=70)
    slug = models.SlugField(max_length=70, unique=True, blank=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    def get_url(self):
        return reverse("article_list", kwargs={
            "slug": self.slug
        })

    @property
    def num_articles(self):
        return Article.objects.filter(categories=self).count()


class Article(models.Model):
    title = models.TextField(blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    cover_image = models.ImageField(blank=True, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    meta_thumbnail = ResizedImageField(
        size=[1200, 600],
        crop=['middle', 'center'],
        quality=75,
        upload_to='thumbnails/',
        blank=True,
        null=True
    )
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        super(Article, self).save(*args, **kwargs)
        if self.cover_image and (not self.meta_thumbnail or self.meta_thumbnail.name != f"{self.cover_image.name}"):
            self.meta_thumbnail.save(
                f"{self.cover_image.name}", self.cover_image, save=False)
            super(Article, self).save(update_fields=['meta_thumbnail'])

    @property
    def get_thumbnail(self):
        return self.meta_thumbnail.url if self.meta_thumbnail else None

    def __str__(self):
        return self.title

    @property
    def get_url(self):
        return reverse("article_detail", kwargs={
            "slug": self.slug
        })
