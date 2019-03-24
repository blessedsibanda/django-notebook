from django.shortcuts import render

from .models import Note

# Create your views here.
def home(request):
    notes = Note.objects.all()
    return render(request, 'home.html', {'notes': notes})
