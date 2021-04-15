from django.urls import path

from home.views import accueil

urlpatterns = [
    path('', accueil, name='accueil')
]