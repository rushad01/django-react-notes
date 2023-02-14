from django.urls import path, include

from core import views

urlpatterns = [
    path('', views.getRoutes),
    path('language/', views.LanguageView.as_view()),
    path('catagory/', views.CatagoryView.as_view()),
    path('notes/', views.NotesView.as_view()),
]
