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

def edit_note(request, id):
    note = get_object_or_404(Note, id=id)
    form = NoteForm(instance=note)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            updated_note = form.save()
            return redirect(reverse('note_detail', kwargs={'id':updated_note.id}))
        return render(request, 'edit_note.html', {'form':form})
    return render(request, 'edit_note.html', {'form':form})

def delete_note(request, id):
    note = get_object_or_404(Note, id=id)
    if request.method == 'POST':
        note.delete()
        return redirect(reverse('home'))
    return render(request, 'delete_note.html', {'note':note})