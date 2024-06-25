from django.db import models


class NewsletterSubscription(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class Homepage(models.Model):
    hero_title = models.CharField(max_length=150, blank=True, null=True)
    hero_paragraph = models.TextField(blank=True, null=True)
    hero_primary_btn = models.CharField(max_length=90, blank=True, null=True)
    hero_secondary_btn = models.CharField(max_length=90, blank=True, null=True)
    hero_image = models.FileField(
        upload_to="homepage/", blank=True, null=True)
    quote = models.TextField(blank=True, null=True)
    feature_1_title = models.CharField(max_length=150, blank=True, null=True)
    feature_1_paragraph = models.TextField(blank=True, null=True)
    feature_1_btn = models.CharField(max_length=50, blank=True, null=True)
    feature_2_title = models.CharField(max_length=150, blank=True, null=True)
    feature_2_paragraph = models.TextField(blank=True, null=True)
    feature_2_btn = models.CharField(max_length=50, blank=True, null=True)
    feature_3_title = models.CharField(max_length=150, blank=True, null=True)
    feature_3_paragraph = models.TextField(blank=True, null=True)
    feature_3_btn = models.CharField(max_length=50, blank=True, null=True)
    feature_4_title = models.CharField(max_length=150, blank=True, null=True)
    feature_4_paragraph = models.TextField(blank=True, null=True)
    feature_4_btn = models.CharField(max_length=50, blank=True, null=True)
    features_image = models.FileField(
        upload_to="homepage/", blank=True, null=True)
    newsletter_subscription = models.CharField(
        max_length=200, blank=True, null=True)
    about_title = models.CharField(max_length=150, blank=True, null=True)
    about_paragraph = models.TextField(blank=True, null=True)
    about_primary_btn = models.CharField(max_length=90, blank=True, null=True)
    about_image = models.ImageField(
        upload_to="homepage/", blank=True, null=True)
    cta = models.CharField(max_length=90, blank=True, null=True)

    def __str__(self):
        return "Home Page"

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Page"
