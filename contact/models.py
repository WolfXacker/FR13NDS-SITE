from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField

class Contact(models.Model):
    имя = models.CharField(max_length=40)
    body =  RichTextField()
    date = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.имя