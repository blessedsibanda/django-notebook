from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import Note

# Create your views here.
def home(request):
    notes = Note.objects.all()
    return render(request, 'home.html', {'notes': notes})

def note_detail(request, id):
    note = get_object_or_404(Note,id=id)
    return render(request, 'detail.html', {'note': note})

def add_note(request):
    if request.method == 'POST':
        title = request.POST.get('title', None)
        content = request.POST.get('content', None)
        new_note = Note(title=title, content=content)
        new_note.save()
        return redirect(reverse('note_detail', kwargs={'id': new_note.id}))
    return render(request, 'add_note.html')