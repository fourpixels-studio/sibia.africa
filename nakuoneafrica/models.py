from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django_resized import ResizedImageField
from django.utils import timezone
from django.contrib.auth.models import User


class SDG(models.Model):
    name = models.CharField(max_length=80)
    description = models.TextField(null=True, blank=True)
    icon = models.CharField(max_length=20)
    slug = models.SlugField(max_length=70, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "SDGs"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(SDG, self).save(*args, **kwargs)

    @property
    def get_url(self):
        return reverse("articles_listed_by_sdg", kwargs={
            "slug": self.slug
        })

    @property
    def num_articles(self):
        return Article.objects.filter(sdg=self).count()


class Article(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    cover_image = models.ImageField(
        upload_to="article_images/", blank=True, null=True)
    attachment = models.FileField(
        upload_to="article_attachments/", blank=True, null=True)
    sdg = models.ForeignKey(
        SDG, on_delete=models.CASCADE, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    meta_thumbnail = ResizedImageField(
        size=[1200, 600],
        crop=['middle', 'center'],
        quality=75,
        upload_to='thumbnails/',
        blank=True,
        null=True
    )
    published_date = models.DateTimeField(
        default=timezone.now, blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

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
