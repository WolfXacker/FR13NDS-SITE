from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from embed_video.fields import EmbedVideoField
from ckeditor.fields import RichTextField

class Article(models.Model):
    title = models.CharField(max_length=40)
    body =  RichTextField()
    url = EmbedVideoField()
    date = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])