from django.shortcuts import render, redirect, reverse
from django.contrib.auth.forms import UserCreationForm


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return redirect(reverse('home'))
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})
