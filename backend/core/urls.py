from django.urls import path, include

from core import views

urlpatterns = [
    path('', views.getRoutes),
    path('languages/', views.LanguageView.as_view()),
    path('catagories/', views.CatagoryView.as_view()),
    path('notes/', views.NotesView.as_view()),
    path('notes/<int:pk>', views.NotesDetail.as_view()),
]
