from django.urls import path 

from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('note/<int:id>/', views.note_detail, name='note_detail'),
    path('note/add/', views.add_note, name='add_note'),
]