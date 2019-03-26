from django.db import models
from django.urls import reverse
from django.conf import settings


class Note(models.Model):
    title = models.CharField(max_length=120, unique=True)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notes')
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='shared_notes')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('note_detail', kwargs={'id': self.id})