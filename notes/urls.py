from django.urls import path 

from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('note/<int:id>/', views.note_detail, name='note_detail'),
    path('note/add/', views.add_note, name='add_note'),
    path('note/<int:id>/edit/', views.edit_note, name='edit_note'),
    path('note/<int:id>/delete/', views.delete_note, name='delete_note'),
    path('note/<int:id>/share/', views.share_note, name='share_note'),
]