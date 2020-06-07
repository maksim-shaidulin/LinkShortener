import datetime
from django.db import models
from django.utils import timezone


class Link(models.Model):
    short_link = models.CharField(
        "Short link", max_length=7, null=False, unique=True)
    full_link = models.CharField("Full link", max_length=500, unique=True, null=False)
    created_at = models.DateTimeField("Created at", auto_now=True)

    def __str__(self):
        return self.short_link

    def is_old(self, days=7):
        return self.created_at < (timezone.now() - datetime.timedelta(days=days))

    class Meta:
        verbose_name = "Link"
        verbose_name_plural = "Links"
