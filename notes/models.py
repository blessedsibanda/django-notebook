from django.db import models
from django.urls import reverse


class Note(models.Model):
    title = models.CharField(max_length=120, unique=True)
    content = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('note_detail', kwargs={'id': self.id})