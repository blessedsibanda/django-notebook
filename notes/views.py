from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404
from django.contrib import messages

from .models import Note
from .forms import NoteForm

# Create your views here.
@login_required
def home(request):
    notes = Note.objects.filter(owner=request.user)
    return render(request, 'home.html', {'notes': notes})

@login_required
def note_detail(request, id):
    note = get_object_or_404(Note,id=id)
    if note.owner == request.user:
        return render(request, 'detail.html', {'note': note})
    else:
        raise Http404('You can only view your own notes')

@login_required
def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            new_note = form.save(commit=False)
            new_note.owner = request.user
            new_note.save()
            return redirect(reverse('note_detail', kwargs={'id':new_note.id}))
    else:
        form = NoteForm()
    return render(request, 'add_note.html', {'form':form})

@login_required
def edit_note(request, id):
    note = get_object_or_404(Note, id=id)
    if note.owner != request.user:
        raise Http404('You can only edit your own notes')
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            updated_note = form.save()
            return redirect(reverse('note_detail', kwargs={'id':updated_note.id}))
    else:
        form = NoteForm(instance=note)
    return render(request, 'edit_note.html', {'form':form})

@login_required
def delete_note(request, id):
    note = get_object_or_404(Note, id=id)
    if note.owner != request.user:
        raise Http404('You can only delete your own notes')
    if request.method == 'POST':
        note.delete()
        return redirect(reverse('home'))
    return render(request, 'delete_note.html', {'note':note})


@login_required
def share_note(request, id):
    note = get_object_or_404(Note, id=id)
    all_users = User.objects.all()
    if request.method == 'POST':
        send_to = []
        counter = 0
        for user in all_users:
            if request.POST.get(user.username, None) and user not in note.users.all():
                note.users.add(user)
                counter += 1
        messages.success(request, f'Shared note with {counter} users')
        return redirect(reverse('note_detail', kwargs={'id': note.id}))
    return render(request, 'share.html',{'note':note, 'users': all_users })
