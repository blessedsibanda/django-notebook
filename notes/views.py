from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import Note
from .forms import NoteForm

# Create your views here.
def home(request):
    notes = Note.objects.all()
    return render(request, 'home.html', {'notes': notes})

def note_detail(request, id):
    note = get_object_or_404(Note,id=id)
    return render(request, 'detail.html', {'note': note})

def add_note(request):
    form = NoteForm()
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            new_note = form.save()
            return redirect(reverse('note_detail', kwargs={'id':new_note.id}))
        return render(request, 'add_note.html', {'form':form})
    return render(request, 'add_note.html', {'form':form})