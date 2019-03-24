from django.shortcuts import render, get_object_or_404

from .models import Note

# Create your views here.
def home(request):
    notes = Note.objects.all()
    return render(request, 'home.html', {'notes': notes})

def note_detail(request, id):
    note = get_object_or_404(Note,id=id)
    return render(request, 'detail.html', {'note': note})