from django.db import models


class RSSFeed(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
