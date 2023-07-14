from django.contrib import admin
from django.urls import path
from ia_art import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/artists/", views.ia_art, name="artists"),
    path("api/artist/<int:id>", views.artist, name="artist"),
]
